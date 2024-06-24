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

## Can I overlay the two graphs?
proto_counts = pd.merge(benign_proto_counts, malicious_proto_counts, on='proto', how='outer').fillna(0)

plt.figure(figsize=(10, 5))
ax = sns.barplot(data=proto_counts, x='proto', y='count_benign', color='#4c72b0', label='Benign')
ax = sns.barplot(data=proto_counts, x='proto', y='count_malicious', color='#dd8452', label='Malicious', alpha=0.7)

plt.title('Comparison of Protocol Usage in Benign and Malicious Traffic')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.legend()

plt.xticks(rotation=45)
## Literally just do it twice, once for each set of data. Not so bad.
for index, row in proto_counts.iterrows():
    ax.text(row.name, row['count_benign'], int(row['count_benign']), color='black', ha="center")
    ax.text(row.name, row['count_malicious'], int(row['count_malicious']), color='black', ha="center", va='bottom')

plt.show()