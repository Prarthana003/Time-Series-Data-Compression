import pandas as pd

# Read the CSV file
df = pd.read_csv('output_with_consecutive_epoch.csv')

# Create a new DataFrame with 'EpochTime' and 'Wind Speed (m/s)' columns
df_subset = df[['EpochTime', 'Wind Speed (m/s)']]

# Write the subset DataFrame to a new CSV file
df_subset.to_csv('epoch_wind_speed.csv', index=False)
