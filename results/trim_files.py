import csv
import os

results = '/home/robb/PycharmProjects/locust-flask-test/results'


def trim_csv_file(filename, rows):
    # Read the CSV file into a list of lists
    with open(filename, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Check if number of rows to keep is within bounds
    if rows > len(data):
        raise ValueError(f"Number of rows to keep ({rows}) exceeds total rows ({len(data)})")

    # Trim the bottom rows
    data_trimmed = data[:rows]

    # Write the trimmed data back to the CSV file
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_trimmed)

    print(f"Trimmed {filename} to keep only the top {rows} rows.")


date = '20240520'
exp_name = 'sin200-1h-vpa'

exp_path_st = f'{results}/{date}/{exp_name}/Service_Time'
exp_path_cpu = f'{results}/{date}/{exp_name}/CPU_Usage'
exp_path_replicas = f'{results}/{date}/{exp_name}/Replicas'
exp_path_rps = f'{results}/{date}/{exp_name}/RPS'
exp_path_request = f'{results}/{date}/{exp_name}/CPU_request_utilization'

# folders = [exp_path_st, exp_path_cpu, exp_path_replicas, exp_path_rps, exp_path_request]
folders = [exp_path_request]

for folder in folders:
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            trim_csv_file(filepath, 61)
