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



### Let's focus on the targetted IP addresses, essentialy the id.resp_h column. First a count of each one.

malicious_resp_ip_counts = malicious_data['id.resp_h'].value_counts().reset_index()
malicious_resp_ip_counts.columns = ['id.resp_h', 'count']

plt.figure(figsize=(10, 5))
bar_plot = sns.barplot(data=malicious_resp_ip_counts.head(20), x='id.resp_h', y='count', palette='colorblind')
plt.title('Targeted IPs in Malicious Traffic')
plt.xlabel('Responding IP')
plt.ylabel('Count of Malicious Events')
plt.xticks(rotation=45)

# Add counts on top of the bars
for index, row in malicious_resp_ip_counts.head(20).iterrows():
    bar_plot.text(index, row['count'], row['count'], color='black', ha="center")

plt.show()
