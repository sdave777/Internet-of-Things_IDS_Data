import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

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


## Let's try a pivot table to see if it shows that I missed anything.

pivot_table = data.pivot_table(values='duration', index='id.resp_h', columns='proto', aggfunc='mean').fillna(0)
plt.figure(figsize=(15, 7))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu')
plt.title('Average Duration by Protocol and Responder IP')
plt.show()
