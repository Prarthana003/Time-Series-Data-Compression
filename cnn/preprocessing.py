import pandas as pd
import json

json_file = 'output.json'

# Load data from JSON file
with open(json_file, 'r') as f:
    data = json.load(f)
window_size = 30
output_file = "preprocessed_data.tsv"

# Extracting the second values (measurements) from the data
measurements = [item[1] for item in data]

# Sliding window function to create windowed sequences
def create_windows(data, window_size):
    windows = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        windows.append(window)
    return windows

# Create sliding windows of measurements
windows = create_windows(measurements, window_size)

# Prepare data for output
output_data = []
for idx, window in enumerate(windows):
    # label = f"Label{idx + 1}"  # Generate label for each window
    row =  window  # Combine label and window values
    output_data.append(row)

# Convert to DataFrame for easier writing to TSV
df = pd.DataFrame(output_data)

# Write DataFrame to TSV file
df.to_csv(output_file, sep='\t', index=False, header=False)

print(f"Preprocessed data saved to {output_file}")
