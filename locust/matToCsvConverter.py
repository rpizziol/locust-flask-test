import scipy.io as sio
import csv

# Load the data from the .mat file
data = sio.loadmat('./trace.mat')

# Extract the data you want to convert (assuming a variable named 'my_data')
data_to_convert = data['users']

# Open a CSV file for writing
with open('trace.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the data to the CSV file
    csv_writer.writerows(data_to_convert)

print('Conversion to CSV completed!')
