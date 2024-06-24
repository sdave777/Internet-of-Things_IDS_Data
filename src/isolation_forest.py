import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

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



## So there is this thing called an isolation forest?

# Ensure 'duration' and 'orig_bytes' exist and are not null
required_columns = ['duration', 'orig_bytes']
data = data[required_columns + [col for col in data.columns if col not in required_columns]].dropna(subset=required_columns)

# Convert duration to minutes
data['duration'] = data['duration'] / 60

# Select numerical data for the model
numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Fit the IsolationForest model
iso_forest = IsolationForest(contamination=0.1)
data['anomaly'] = iso_forest.fit_predict(numerical_data)

# Ensure 'duration' and 'orig_bytes' are used for plotting
if 'duration' in data.columns and 'orig_bytes' in data.columns:
    sns.scatterplot(data=data, x='duration', y='orig_bytes', hue='anomaly', palette='coolwarm')
    plt.title('Anomaly Detection using Isolation Forest')
    plt.xlabel('Duration (Minutes)')
    plt.ylabel('Origin Bytes')
    plt.show()
else:
    print("Columns 'duration' and 'orig_bytes' must exist in the DataFrame.")
