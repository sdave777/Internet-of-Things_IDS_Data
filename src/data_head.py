import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Let's look at the data.

data = pd.read_csv('../data/IOTNET24_IDS.csv').drop('Unnamed: 0', axis=1)

## The duration column is in seconds. Let's convert it to minutes.

data['duration'] = data['duration'] / 60

print(data.sample(30))