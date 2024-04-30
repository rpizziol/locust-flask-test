import math
import csv
from utils import plot_csv


def generate_sin(filename, min_value, max_value, phase_shift, period, num_entries):
    amplitude = (max_value - min_value) / 2
    vertical_shift = min_value + amplitude

    frequency = num_entries / period
    data = []

    # Generate data points for the sin wave
    for i in range(num_entries):
        x = i / (num_entries - 1)  # Normalize x-axis values between 0 and 1
        y = amplitude * math.sin(2 * math.pi * frequency * x + phase_shift) + vertical_shift
        data.append([int(y)])  # Store x and y values in a list

    # Open a CSV file for writing
    with open(f"./workloads/{filename}", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)  # Write data points


generate_sin('./sin_test.csv', 10, 80, 0, 200, 2000)
plot_csv('workloads/sin_test.csv')
