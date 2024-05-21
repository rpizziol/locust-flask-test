import csv

results = '/home/robb/PycharmProjects/locust-flask-test/results'


def clean_gcloud_csvs(filepath, new_label):
    # Read the CSV file
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    data.pop(1)  # Remove the second row
    data[0][1] = new_label  # Rename the second column to "Usage"

    # Write the modified data to a new CSV file
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_average_RPS_csv(date, exp_name):
    file_paths = [f'{results}/{date}/{exp_name}/RPS/RPS_1.csv',
                  f'{results}/{date}/{exp_name}/RPS/RPS_2.csv',
                  f'{results}/{date}/{exp_name}/RPS/RPS_3.csv']

    # Output file path
    output_file = f'{results}/{date}/{exp_name}/RPS/RPS_4.csv'

    # Dictionary to store TimeSeries ID and average RPS
    average_rps = {}

    # Read and process each CSV file
    for file_path in file_paths:
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row (assuming the first row is header)
            for row in reader:
                time_series_id = row[0]
                rps_value = float(row[1])

                # Add or update the average for the TimeSeries ID
                if time_series_id in average_rps:
                    average_rps[time_series_id] += rps_value
                else:
                    average_rps[time_series_id] = rps_value

    # Calculate the average RPS for each TimeSeries ID
    for time_series_id, total_rps in average_rps.items():
        average_rps[time_series_id] /= len(file_paths)  # Divide by number of files

    # Write the results to a new CSV file
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["TimeSeries ID", "RPS"])  # Write header row
        for time_series_id, average_value in average_rps.items():
            writer.writerow([time_series_id, average_value])


def clean_full_project(results, date, exp_name):
    project_path = f'{results}/{date}/{exp_name}'
    for i in range(1, 5):
        # clean_gcloud_csvs(f'{project_path}/CPU_Usage/CPU_Usage_{i}.csv',
        #                   'Usage')
        # clean_gcloud_csvs(f'{project_path}/Replicas/Replicas_{i}.csv',
        #                   'Replicas')
        clean_gcloud_csvs(f'{project_path}/CPU_request_utilization/CPU_request_utilization_{i}.csv', 'Request')

    # for i in range(1, 4):
    #     clean_gcloud_csvs(f'{project_path}/RPS/RPS_{i}.csv',
    #                       'RPS')
    #     clean_gcloud_csvs(f'{project_path}/Service_Time/Service_Time_{i}.csv', 'Service Time')
    #
    # generate_average_RPS_csv(date, exp_name)


clean_full_project(results, '20240520', 'sin200-1h-vpa')
