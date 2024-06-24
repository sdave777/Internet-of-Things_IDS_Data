import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipinfo

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


## I found a geolocation library that I think is interesting, let's try it out.

# Replace 'your_access_token' with your actual IPinfo access token
access_token = 'insert token here'
handler = ipinfo.getHandler(access_token)


# Function to get geolocation data for an IP address
def get_geolocation(ip):
    try:
        if pd.isna(ip):
            return {
                'latitude': None,
                'longitude': None,
                'country': None,
                'city': None
            }
        details = handler.getDetails(ip)
        return {
            'latitude': details.all.get('latitude'),
            'longitude': details.all.get('longitude'),
            'country': details.all.get('country_name'),
            'city': details.all.get('city')
        }
    except Exception as e:
        return {
            'latitude': None,
            'longitude': None,
            'country': None,
            'city': None
        }

# Apply the function to the DataFrame
geolocation_data = data['id.resp_h'].apply(get_geolocation)
geolocation_df = pd.DataFrame(geolocation_data.tolist())
data = pd.concat([data, geolocation_df], axis=1)

for idx, row in geolocation_df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    city = row['city']
    country = row['country']
    if latitude is not None and longitude is not None:
        print(f"IP Address: {data['id.resp_h'][idx]}, City: {city}, Country: {country}, Latitude: {latitude}, Longitude: {longitude}")
    else:
        print(f"IP Address: {data['id.resp_h'][idx]} has incomplete geolocation data.")