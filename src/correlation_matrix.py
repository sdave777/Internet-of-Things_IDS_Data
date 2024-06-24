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



## Maybe a correlation matrix would be interesting.

## I had to change some values for this to work. This is where the binary thing comes in handy.

label = {'Malicious': 1,'Benign': 0}
data.label = [label[item] for item in data.label]

protocol = {'tcp': 1,'udp': 0}
data.proto = [protocol[item] for item in data.proto]

## Let's just drop those columns we don't need.

cleaned = data.drop(['id.orig_h', 'id.resp_h', 'service', 'conn_state', 'history'], axis=1)


plt.figure(figsize=(12, 8))

corr = cleaned.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(cleaned.corr(), annot=True, mask=mask, cmap='coolwarm', fmt=".2f")

plt.xticks(rotation=45)
