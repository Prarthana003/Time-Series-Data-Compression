import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('output_with_consecutive_epoch.csv')

# Select the first 50 instances
df_subset = df.head(400)

# Plot consumption vs. EpochTime for the first 50 instances
plt.figure(figsize=(10, 6))
plt.plot(df_subset['EpochTime'], df_subset['Wind Speed (m/s)'], marker='o', linestyle='-')
plt.title('Consumption vs. Epoch Time (First 200 Instances)')
plt.xlabel('Epoch Time')
plt.ylabel('Consumption')
plt.grid(True)

# Save the plot as an image file (e.g., PNG)
plt.savefig('consumption_vs_epoch_time_first_50.png')

# Display the plot
plt.show()
