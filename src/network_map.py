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


## A network map would be extremely useful.

G = nx.from_pandas_edgelist(data, 'id.orig_h', 'id.resp_h', ['duration'])
plt.figure(figsize=(10, 5))
pos = nx.spring_layout(G, k=0.1)
nx.draw(G, pos, with_labels=True, node_size=20, node_color='blue', font_size=8, edge_color='gray')
plt.title('Network Graph of Origin and Responder IPs')
plt.show()
