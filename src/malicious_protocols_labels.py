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

## I like the labels on the benign graph, so let's do to malicious values that way too.
malicious_proto_counts = malicious_data['proto'].value_counts().reset_index()
malicious_proto_counts.columns = ['proto', 'count_malicious']

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=malicious_proto_counts, x='proto', y='count_malicious')
plt.title('Distribution of Protocols in Malicious Traffic')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.xticks(rotation=45)

for index, row in malicious_proto_counts.iterrows():
    ax.text(row.name, row['count_malicious'], round(row['count_malicious'], 2), color='black', ha="center")

plt.show()