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


## Now for the responder bytes of data.

malicious_data['resp_bytes_kb'] = malicious_data['resp_bytes'] / 1024

# Identify the event with the largest resp_bytes_kb
largest_resp_bytes_event = malicious_data.loc[malicious_data['resp_bytes_kb'].idxmax()]

plt.figure(figsize=(10, 5))
scatter_plot = sns.scatterplot(data=malicious_data, x='duration', y='resp_bytes_kb', hue='conn_state', palette='colorblind', legend='full')
sns.kdeplot(data=malicious_data, x='duration', y='resp_bytes_kb', hue='conn_state', levels=5, fill=True, alpha=0.3)
plt.title('Duration vs. Responder Bytes for Malicious Traffic')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Responder Bytes (KB)')

# Annotate the largest resp_bytes_kb event with the value in kilobytes
plt.annotate(f'{largest_resp_bytes_event["resp_bytes_kb"]:.2f} KB',
             xy=(largest_resp_bytes_event['duration'], largest_resp_bytes_event['resp_bytes_kb']),
             xytext=(largest_resp_bytes_event['duration'], largest_resp_bytes_event['resp_bytes_kb']-0.50),
             fontsize=12, color='red', ha='center', va='top')

s1_connections = malicious_data[malicious_data['conn_state'] == 'S1']
for _, row in s1_connections.iterrows():
    plt.annotate('S1', xy=(row['duration'], row['resp_bytes_kb']), xytext=(row['duration'], row['resp_bytes_kb'] + 0.25),
                 fontsize=10, color='blue', ha='center', va='bottom')

# Set the x-axis to start at 0
plt.xlim(left=-10)
plt.ylim(bottom=0)

legend_labels = {
    'S0': 'S0 = Connection attempt seen, no reply',
    'S3': 'S3 = Connection established, close attempt by responder seen, \n         no reply from originator',
    'RSTR': 'RSTR = Responder sent a RST',
    'S1': 'S1 = Connection established, not terminated',
    'OTH': 'OTH = No SYN seen, just midstream traffic'
}

# Get the current handles and labels
handles, labels = plt.gca().get_legend_handles_labels()

# Replace the labels with the custom labels
new_labels = [legend_labels.get(label, label) for label in labels]

# Create the custom legend
plt.legend(handles, new_labels, title='Connection State', loc='lower right')

plt.show()