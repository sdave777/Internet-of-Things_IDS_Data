import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Honestly, I only really care about malicious data, let's select for that.

data = pd.read_csv('../data/IOTNET24_IDS.csv').drop('Unnamed: 0', axis=1)

data['duration'] = data['duration'] / 60

malicious_data = data[data['label'] != 'Benign'].copy()

malicious_data['duration'] = malicious_data['duration'].astype(float)

malicious_data['event_index'] = malicious_data.index

# print(malicious_data.head())

# Just in case I need benign data later, I'll save it as well.

benign_data = data[data['label'] == 'Benign'].copy()

# print(benign_data.head())

# I think this longest duration event is interesting, let's keep it.

longest_duration_event = malicious_data.loc[malicious_data['duration'].idxmax()]

longest_duration_event_number = longest_duration_event['event_index']
#print(f'The event number for the longest duration data point is: {longest_duration_event_number}')



# Okay so the IP is 185.244.25.235, so let's filter for that.

filtered_data = malicious_data[malicious_data['id.resp_h'] == '185.244.25.235']

# Assuming the duration is already in minutes, so no conversion is needed
# Create a column for the index to use as the x-axis
filtered_data['event_index'] = filtered_data.index

# Plot the scatter plot for duration of each event
plt.figure(figsize=(10, 5))
scatter_plot = sns.scatterplot(data=filtered_data, x='event_index', y='duration', hue='conn_state', palette='colorblind', legend='full')
plt.title('Events for IP Address 185.244.25.235')
plt.xlabel('Event Number')
plt.ylabel('Duration (Minutes)')

# Create the custom legend
legend_labels = {
    'S0': 'S0 = Connection attempt seen, no reply',
    'SF': 'SF = Normal establishment and termination',
    'S3': 'S3 = Connection established, close attempt by responder seen, \n         no reply from originator',
    'RSTR': 'RSTR = Responder sent a RST',
    'S1': 'S1 = Connection established, not terminated',
    'OTH': 'OTH = No SYN seen, just midstream traffic'
}

handles, labels = scatter_plot.get_legend_handles_labels()
new_labels = [legend_labels.get(label, label) for label in labels]
plt.legend(handles, new_labels, title='Connection State', loc='upper right')

plt.show()
