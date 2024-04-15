import scipy.io as sio
import csv
import math
import pandas as pd
import matplotlib.pyplot as plt


def convert_mat_to_csv(in_path, out_path):
    data = sio.loadmat(in_path)
    data_to_convert = data['users'].T

    with open(out_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data_to_convert)


def generate_sin_csv(filename, min_value, max_value, phase_shift, frequency, num_entries):
    amplitude = (max_value - min_value) / 2
    vertical_shift = min_value + amplitude

    data = []

    # Generate data points for the sin wave
    for i in range(num_entries):
        x = i / (num_entries - 1)  # Normalize x-axis values between 0 and 1
        y = amplitude * math.sin(2 * math.pi * frequency * x + phase_shift) + vertical_shift
        data.append([y])  # Store x and y values in a list

    # Open a CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)  # Write data points


def plot_csv(filename):
    # Read the CSV file. Assuming no header and the data is in the first column.
    data = pd.read_csv(filename, header=None)

    # Plotting
    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    plt.plot(data, marker='o', linestyle='-', color='b')  # Line plot

    plt.title(filename)  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel('Users')  # Optional: Adds a label to the y-axis
    plt.show()
