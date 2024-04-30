import csv


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


results_path = '/home/robb/PycharmProjects/locust-flask-test/results'
project_path = f'{results_path}/20240429/muopt-w30-sin_p400-30min'
for i in range(1, 5):
    clean_gcloud_csvs(f'{project_path}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_{i}.csv',
                      'Usage')
    clean_gcloud_csvs(f'{project_path}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_{i}.csv',
                      'Replicas')

for i in range(1, 4):
    clean_gcloud_csvs(f'{project_path}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_{i}.csv',
                      'RPS')
    clean_gcloud_csvs(f'{project_path}/Service_Time_(ms)/Service_Time_(ms)_{i}.csv', 'Service Time')
