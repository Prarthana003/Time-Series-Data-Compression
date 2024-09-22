import numpy as np
import matplotlib.pyplot as plt

# Define the file name
file_name = "periodic.tsv"

# Open the file in read mode
with open(file_name, "r") as file:
    lines = file.readlines()

# Extract the time series data for the first instance
time_series_data = lines[0].strip().split("\t")
time_series_data = [float(value) for value in time_series_data]

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(time_series_data)
plt.title("Time Series Data (First Instance)")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.grid(True)
plt.show()
