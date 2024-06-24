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

## Some labels would help that last plot, let's add them.

longest_duration_event = malicious_data.loc[malicious_data['duration'].idxmax()]

# Convert the longest duration to hours
longest_duration_hours = longest_duration_event['duration'] / 60

# Filter S1 connections
s1_connections = malicious_data[malicious_data['conn_state'] == 'S1']

plt.figure(figsize=(10, 5))
scatter_plot = sns.scatterplot(data=malicious_data, x='event_index', y='duration', hue='conn_state', palette='colorblind', legend='full')
plt.title('Malicious Traffic Events')
plt.xlabel('Event Number')
plt.ylabel('Duration (Minutes)')

# Annotate the longest duration event with the duration in hours
plt.text(longest_duration_event['event_index'], longest_duration_event['duration'] - 50,
         f'{longest_duration_hours:.2f} hours', fontsize=12, color='red', ha='right')

# Highlight S1 connections with text annotations
for _, row in s1_connections.iterrows():
    plt.text(row['event_index'], row['duration'] + 10, 'S1', fontsize=10, color='blue', ha='center', va='bottom')

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