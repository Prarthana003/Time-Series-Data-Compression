import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('epoch_wind_speed.csv')

# Create an empty list to store the data
data_list = []

# Iterate through the rows and construct the list of lists
for index, row in df.iterrows():
    epoch_time = int(row['EpochTime'])
    wind_speed = row['Wind Speed (m/s)']
    data_list.append([epoch_time, wind_speed])

# Write the list to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data_list, json_file)
