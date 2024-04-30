import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_csv(filename, index, exp_name):
    data = pd.read_csv(filename)
    column = data[index]
    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    # plt.step(np.linspace(1,200,200), data, marker='o', linestyle='-', color='b')  # Line plot
    plt.step(np.linspace(1, column.size, column.size), column, linestyle='-')
    plt.title(f"{index} vs Time")  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel(index)  # Optional: Adds a label to the y-axis
    # Save the plot to a PDF file
    plt.savefig(f'{exp_name}_{index.replace(" ", "").replace("/", "-")}_plot.pdf')
    plt.show()


def plot_usage(filename1, filename2, filename3, exp_name):
    index = 'Usage'
    data1 = pd.read_csv(filename1)
    data2 = pd.read_csv(filename2)
    data3 = pd.read_csv(filename3)
    column1 = data1[index]
    column2 = data2[index]
    column3 = data3[index]

    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    # plt.step(np.linspace(1,200,200), data, marker='o', linestyle='-', color='b')  # Line plot
    plt.plot(np.linspace(1, column1.size, column1.size), column1, linestyle='-', label='Tier1')
    plt.plot(np.linspace(1, column2.size, column2.size), column2, linestyle='-', label='Tier2')
    plt.plot(np.linspace(1, column3.size, column3.size), column3, linestyle='-', label='Tier3')
    plt.title(f"{index} vs Time")  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel(index)  # Optional: Adds a label to the y-axis
    # Save the plot to a PDF file
    plt.savefig(f'{exp_name}_{index.replace(" ", "").replace("/", "-")}_plot.pdf')
    plt.show()

#
# day_folder = '20240416'
# exp_name = 'sin-users80-min60'
#
# filepath = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/{exp_name}_stats_history.csv'
#
# plot_csv(filepath, 'User Count', exp_name)
# plot_csv(filepath, 'Requests/s', exp_name)
# plot_csv(filepath, 'Total Average Response Time', exp_name)
#
# gcloud_filepath = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# gcloud_usage_filepath_1 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_1.csv'
# gcloud_usage_filepath_2 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_2.csv'
# gcloud_usage_filepath_3 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_3.csv'
# plot_csv(gcloud_filepath, 'Replicas', exp_name)
# plot_usage(gcloud_usage_filepath_1, gcloud_usage_filepath_2, gcloud_usage_filepath_3, exp_name)

data = pd.read_csv('./sin160.csv')
plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
plt.plot(data)
#plt.step(np.linspace(1, column.size, column.size), column, linestyle='-')
# plt.title(f"Users vs Time")  # Optional: Adds a title to the plot
# plt.xlabel('Time')  # Optional: Adds a label to the x-axis
# plt.ylabel('Users')  # Optional: Adds a label to the y-axis
# Save the plot to a PDF file
# plt.savefig(f'{exp_name}_{index.replace(" ", "").replace("/", "-")}_plot.pdf')
plt.show()