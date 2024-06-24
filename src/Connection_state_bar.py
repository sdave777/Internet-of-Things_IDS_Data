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



### I like how that last one looks, let's do it for the connection states as well.

plt.figure(figsize=(10, 5))
sns.countplot(data=malicious_data, x='conn_state', palette='viridis')
plt.title('Count of Connection States in Malicious Traffic')
plt.xlabel('Connection State')
plt.ylabel('Count')
plt.show()
