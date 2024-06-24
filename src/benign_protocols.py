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

## Now benign traffic protocols.

benign_proto_counts = benign_data['proto'].value_counts().reset_index()
benign_proto_counts.columns = ['proto', 'count_benign']

custom_colors = ['#55a868', '#4c72b0']

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=benign_proto_counts, x='proto', y='count_benign', palette=custom_colors)
plt.title('Distribution of Protocols in Benign Traffic')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.xticks(rotation=45)

##Some labels would be nice, I don't why it says there is an error, this works everytime for me

for index, row in benign_proto_counts.iterrows():
    ax.text(row.name, row['count_benign'], round(row['count_benign'], 2), color='black', ha="center")

plt.show()