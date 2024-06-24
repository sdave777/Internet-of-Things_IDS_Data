import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Not sure where to start... Let's do some histograms.

data = pd.read_csv('../data/IOTNET24_IDS.csv').drop('Unnamed: 0', axis=1)

data['duration'] = data['duration'] / 60

data.hist(figsize=(15, 10))
plt.show()