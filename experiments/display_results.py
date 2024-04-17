import pandas as pd
import matplotlib.pyplot as plt


def plot_dual_axis(csv_file1, csv_file2):
    # Read the data from the first CSV file
    data1 = pd.read_csv(csv_file1, header=0, names=['time', 'Cores_per_replica'], parse_dates=['time'])
    # Read the data from the second CSV file
    data2 = pd.read_csv(csv_file2, header=0, names=['time', 'Users'], parse_dates=['time'])

    # Create a plot with a figure and one axis
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first dataset with the first y-axis
    ax1.plot(data1['time'], data1['Cores_per_replica'], color='tab:blue', label='Cores per Replica')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Total Cores', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second y-axis for the second dataset
    ax2 = ax1.twinx()
    ax2.plot(data2['time'], data2['Users'], color='tab:red', label='Users')
    ax2.set_ylabel('Number of Users', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Adding titles and legends
    fig.tight_layout()
    plt.title('Cores and Users Over Time')
    # fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    plt.show()


cores_data = './data/20240415-2/SpringTestApp_3Tier_-_Cores_per_replica/SpringTestApp_3Tier_-_Cores_per_replica_4.csv'
users_data = './data/20240415-2/workload_sin900.csv'

# Example usage with the specific file names
plot_dual_axis(cores_data, users_data)
