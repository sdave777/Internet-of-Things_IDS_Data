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

## Now I'd like to plot the duration of events in a scatter.

plt.figure(figsize=(10, 5))

# I think I can change color by connection state.

scatter_plot = sns.scatterplot(data=malicious_data, x='event_index', y='duration', palette='colorblind', hue='conn_state', legend='full')
plt.title('Malicious Traffic Events')
plt.xlabel('Event Number (Out of 23145)')
plt.ylabel('Duration (Minutes)')

# Cleaned up the legend a bit.

legend_labels = {
    'S0': 'S0 = Connection attempt seen, no reply',
    'S3': 'S3 = Connection established, close attempt by responder seen, \n         no reply from originator',
    'RSTR': 'RSTR = Responder sent a RST',
    'S1': 'S1 = Connection established, not terminated',
    'OTH': 'OTH = No SYN seen, just midstream traffic'
}

# Get the current handles and labels
handles, labels = scatter_plot.get_legend_handles_labels()

# Replace the labels with the custom labels
new_labels = [legend_labels.get(label, label) for label in labels]

# Create the custom legend
scatter_plot.legend(handles, new_labels, title='Connection State', loc='upper right')

plt.show()