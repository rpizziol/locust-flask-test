import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_csv(filename, index):
    data = pd.read_csv(filename)
    column = data[index]  # [0:399]
    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    # plt.step(np.linspace(1,200,200), data, marker='o', linestyle='-', color='b')  # Line plot
    plt.step(np.linspace(1, column.size, column.size), column, linestyle='-')
    plt.title(f"{index} vs Time")  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel(index)  # Optional: Adds a label to the y-axis
    # Save the plot to a PDF file
    # plt.savefig(f'{exp_name}_{index.replace(" ", "").replace("/", "-")}_plot.pdf')
    plt.show()
    return column.mean()


def obtain_workload(filename):
    data = pd.read_csv(filename)
    return data['Requests/s'] * data['Total Average Response Time'] / 1000


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


# day_folder = '20240419'
# exp_name = 'mytest'
#
#
#
# filepath = f'/home/robb/PycharmProjects/locust-flask-test/results/{day_folder}/{exp_name}/{exp_name}_stats_history.csv'
# # filepath = '/home/robb/PycharmProjects/locust-flask-test/results/20240419/mytest/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# filepath_hpa = '/home/robb/PycharmProjects/locust-flask-test/z_old/instance-1/results/20240416/sin-users80-min60/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
#
# # plot_csv(filepath, 'Failures/s', exp_name)
# # plot_csv(filepath_hpa, 'Replicas', exp_name)
#
# plot_csv('/home/robb/PycharmProjects/locust-flask-test/results/20240419/muopt60min2/muopt60min2_stats_history.csv',
#          'Requests/s', 'mytest')
# plot_csv('/home/robb/PycharmProjects/locust-flask-test/z_old/instance-1/results/20240416/sin-users80-min60/sin-users80-min60_stats_history.csv', 'Requests/s', 'mytest')
# plot_csv('/home/robb/PycharmProjects/locust-flask-test/results/20240419/mytest/temp/SpringTestApp_3Tier_-_Replicas_muOpt.csv', 'Replicas', 'mytest')
# plot_csv(filepath, 'Requests/s', exp_name)
# plot_csv(filepath, 'Total Average Response Time', exp_name)
#
# gcloud_filepath = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# gcloud_usage_filepath_1 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_1.csv'
# gcloud_usage_filepath_2 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_2.csv'
# gcloud_usage_filepath_3 = f'/home/robb/PycharmProjects/locust-flask-test/instance-1/results/{day_folder}/{exp_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_3.csv'
# plot_csv(gcloud_filepath, 'Replicas', exp_name)
# plot_usage(gcloud_usage_filepath_1, gcloud_usage_filepath_2, gcloud_usage_filepath_3, exp_name)


locust_muopt = '/home/robb/PycharmProjects/locust-flask-test/results/20240419/muopt60min2/muopt60min2_stats_history.csv'
locust_hpa = '/home/robb/PycharmProjects/locust-flask-test/z_old/instance-1/results/20240416/sin-users80-min60/sin-users80-min60_stats_history.csv'
#
# avg_muopt = plot_csv(locust_muopt, 'Requests/s')
# avg_hpa = plot_csv(locust_hpa, 'Requests/s')
#
# print("Requests/s")
# print(f"avg_muOpt = {avg_muopt}")
# print(f"avg_hpa = {avg_hpa}")
# print(f"incremento = {((avg_hpa - avg_muopt) / avg_hpa) * 100}%")
#
# locust_muopt = '/home/robb/PycharmProjects/locust-flask-test/results/20240419/muopt60min2/SpringTestApp_3Tier_-_Replicas.csv'
# locust_hpa = '/home/robb/PycharmProjects/locust-flask-test/z_old/instance-1/results/20240416/sin-users80-min60/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
#
# avg_muopt = plot_csv(locust_muopt, 'Replicas')
# avg_hpa = plot_csv(locust_hpa, 'Replicas')
#
# print("Replicas")
# print(f"avg_muOpt = {avg_muopt}")
# print(f"avg_hpa = {avg_hpa}")
# print(f"incremento = {((avg_hpa - avg_muopt) / avg_hpa) * 100}%")


data = pd.read_csv(locust_hpa)
workload_hpa = data['User Count']

plt.plot(obtain_workload(locust_hpa), label='Stimato')
plt.plot(workload_hpa, label='Da Locust')
plt.legend()
plt.title("HPA")
plt.show()

data = pd.read_csv(locust_muopt)
workload_muopt = data['User Count']

plt.plot(obtain_workload(locust_muopt))
plt.plot(workload_muopt, label='Da Locust')
plt.title("muOpt")
plt.show()