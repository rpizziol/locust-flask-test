import scipy.io as sio
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def convert_mat_to_csv(in_path, out_path):
    data = sio.loadmat(in_path)
    data_to_convert = data['users'].T

    with open(out_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data_to_convert)


def plot_csv(filename):
    # Read the CSV file. Assuming no header and the data is in the first column.
    data = pd.read_csv(filename, header=None)

    n_data = data.shape[0]

    # Plotting
    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    plt.step(np.linspace(1, n_data, n_data), data, marker='o', linestyle='-', color='b')  # Line plot

    plt.title(filename)  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel('Users')  # Optional: Adds a label to the y-axis
    plt.show()
