import numpy as np

num_instances_per_period = 30  # Number of instances per period length
series_length = 30
num_period_lengths = 8  # Number of different period lengths

# Define the range of period lengths for each instance
period_lengths = np.random.randint(1, 8, num_period_lengths)

# Define the file name
file_name = "periodic.tsv"

# Open the file in write mode
with open(file_name, "w") as file:
    # Generate data for each period length
    for period_length in period_lengths:
        # Generate data for multiple instances with the same period length
        for _ in range(num_instances_per_period):
            # Generate the time series data with a periodic pattern and a random phase shift
            phase_shift = np.random.uniform(0, 2 * np.pi)
            time_series = []
            for t in range(series_length):
                value = np.sin(2 * np.pi * t / period_length + phase_shift)  # Generate a sine wave with the current period length and phase shift
                time_series.append(value)
            
            # Concatenate the label and time series data into a single string
            data_line = "{}\t{}\n".format(period_length, '\t'.join(map(str, time_series)))
            
            # Write the generated data line to the file
            file.write(data_line)

print(f"Data has been written to {file_name}")
