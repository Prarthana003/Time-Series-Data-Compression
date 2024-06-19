import pandas as pd
from datetime import datetime
import time

# Read the CSV file
df = pd.read_csv('T1.csv')

# Assuming the column name is 'DateTime', convert it to datetime objects
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%d %m %Y %H:%M')

# Define a starting point for epoch time (e.g., January 1, 1970)
start_time = datetime(1970, 1, 1)

# Calculate consecutive epoch timestamps based on the row index
df['EpochTime'] = (df.index * 60).astype(int)  # Assuming each row represents a minute

# Write the DataFrame with epoch timestamps to a new CSV file
df.to_csv('output_with_consecutive_epoch.csv', index=False)
