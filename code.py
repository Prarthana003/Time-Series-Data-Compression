import pandas as pd
import matplotlib.pyplot as plt

# Path to the preprocessed data file (TSV format)
tsv_file = "preprocessed_data.tsv"

# Read the TSV file into a DataFrame
df = pd.read_csv(tsv_file, sep='\t', header=None)

# Extract label and measurement columns for the first five instances
num_instances = 5
labels = df.iloc[:num_instances, 0]  # First column contains labels
measurements = df.iloc[:num_instances, 1:]  # Remaining columns contain measurement values

# Plotting each instance's time series data in separate plots
for i in range(num_instances):
    plt.figure(figsize=(8, 4))  # Adjust the figure size for each plot
    plt.plot(measurements.iloc[i, :], label=labels.iloc[i])
    plt.xlabel('Time Step')
    plt.ylabel('Measurement Value')
    plt.title(f'Time Series Data - {labels.iloc[i]}')
    plt.legend()
    plt.grid(True)
    plt.show()
