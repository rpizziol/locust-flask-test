import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def prepare_for_group_plot(filename, index, label):
    data = pd.read_csv(filename)
    column = data[index]
    plt.step(np.linspace(1, column.size, column.size), column, linestyle='-', label=label)
    return column


def plot_csv(filename, index, outfile, label):
    data = pd.read_csv(filename)
    column = data[index]  # [0:399]
    plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
    plt.step(np.linspace(1, column.size, column.size), column, linestyle='-', label=label)
    plt.title(f"{index} vs Time")  # Optional: Adds a title to the plot
    plt.xlabel('Time')  # Optional: Adds a label to the x-axis
    plt.ylabel(index)  # Optional: Adds a label to the y-axis
    plt.savefig(outfile)
    plt.legend()
    plt.show()
    return column.mean()


# def mean_RPS_value(filename):
#     data = pd.read_csv(filename)
#     column = data['RPS'].iloc[2:-2]
#     return column.mean()


# rps1 = '/home/robb/PycharmProjects/locust-flask-test/results/20240422/test_RPS2/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_1.csv'
# rps2 = '/home/robb/PycharmProjects/locust-flask-test/results/20240422/test_RPS2/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_2.csv'
# rps3 = '/home/robb/PycharmProjects/locust-flask-test/results/20240422/test_RPS2/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_3.csv'
#
# print((mean_RPS_value(rps1) + mean_RPS_value(rps2) + mean_RPS_value(rps3)) / 3)
#
# plot_csv(rps1, 'RPS')

#
# test1 = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-window30/muopt-window30_stats_history.csv'
# test2 = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-errorsfix2/muopt-w30-errorsfix2_stats_history.csv'
# test3 = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-errorsfix3/muopt-w30-errorsfix3_stats_history.csv'
# test4 = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-tt1-noerrors/muopt-w30-tt1-noerrors_stats_history.csv'

# plot_csv(test1, 'Requests/s')
# # plot_csv(test2, 'Requests/s')
#
# index = 'Requests/s'
# muopt_1000s_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-1000s/muopt-w30-1000s_stats_history.csv'
# hpa_1000s_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-1000s/HPA-1000s_stats_history.csv'
#
# plt.figure(figsize=(10, 6))  # Optional: Adjusts the figure size
#
# # prepare_for_group_plot(test1, index, 'Normal')
# # prepare_for_group_plot(test2, index, 'Errors disabled')
# # prepare_for_group_plot(test3, index, 'Errors disabled 2')
# # prepare_for_group_plot(test4, index, 'Fixed think time')
# prepare_for_group_plot(muopt_1000s_rps, index, 'muOpt')
# prepare_for_group_plot(hpa_1000s_rps, index, 'HPA')
#
#
# # plt.step(np.linspace(1, column2.size, column2.size), column2, linestyle='-', label='Errors disabled')
# # plt.step(np.linspace(1, column3.size, column3.size), column3, linestyle='-', label='Errors disabled 2')
# plt.title(f"{index} vs Time")  # Optional: Adds a title to the plot
# plt.xlabel('Time')  # Optional: Adds a label to the x-axis
# plt.ylabel(index)  # Optional: Adds a label to the y-axis
# plt.legend()
# # Save the plot to a PDF file
# # plt.savefig(f'{exp_name}_{index.replace(" ", "").replace("/", "-")}_plot.pdf')
# plt.savefig('muOpt-w30_vs_HPA_1000s_thinktime1s.pdf')
# plt.show()

def compare_2autoscalers(filename1, filename2, label1, label2, index):
    column1 = prepare_for_group_plot(filename1, index, label1)
    column2 = prepare_for_group_plot(filename2, index, label2)
    plt.title(f"{index} vs Time")
    plt.xlabel('Time')
    plt.ylabel(index)
    plt.legend()
    plt.savefig(f"./pdfs/{index.replace('/', '')}_{label1}_vs_{label2}.pdf")
    plt.show()
    print(f"Mean {index}")
    print(f"{label1} = {round(column1.mean(), 2)}")
    print(f"{label2} = {round(column2.mean(), 2)}")
    ratio = (round(column2.mean()/column1.mean(), 2)-1) * 100
    print(f"Ratio = {label2} vs {label1}: +{ratio}%")


def compare_3autoscalers(filename1, filename2, filename3, label1, label2, label3, index, outfile):
    column1 = prepare_for_group_plot(filename1, index, label1)
    column2 = prepare_for_group_plot(filename2, index, label2)
    column3 = prepare_for_group_plot(filename3, index, label3)
    plt.title(f"{index} vs Time")
    plt.xlabel('Time')
    plt.ylabel(index)
    plt.legend()
    plt.savefig(outfile)
    plt.show()

    print(f"Mean {index}")
    print(f"{label1} = {round(column1.mean(), 2)}")
    print(f"{label2} = {round(column2.mean(), 2)}")
    print(f"{label3} = {round(column3.mean(), 2)}")


#
# muopt_1000s_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-1000s/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# hpa_1000s_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-1000s/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# compare_muOpt_HPA(hpa_1000s_replicas, hpa_1000s_replicas, 'Replicas', 'muOpt-w30_vs_HPA_15m-20u_thinktime1s_replicas.pdf')
#
# # muopt_1000s_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-w30-1000s/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# hpa_1000s_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-1000s/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# compare_muOpt_HPA(hpa_1000s_usage, hpa_1000s_usage, 'Usage', 'muOpt-w30_vs_HPA_15m-20u_thinktime1s_usage.pdf')
#
#
# muopt_locust = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-15min/muopt-15min_stats_history.csv'
# hpa_locust = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/HPA-15m_stats_history.csv'
# # plot_csv(hpa_locust, 'Requests/s', 'HPA-thr-15m-20u.pdf', 'HPA')
# compare_muOpt_HPA(muopt_locust, hpa_locust, 'muOpt', 'HPA', 'Requests/s', 'muopt-HPA-rps-15m-20u.pdf')
#
#
# hpa_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# muopt_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-15min/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# compare_muOpt_HPA(muopt_usage, hpa_usage, 'muOpt', 'HPA', 'Usage', 'muopt-HPA-Usage-15m-20u.pdf')
#
#
# # DIFFERENT muOpts
#
# muopt_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-sin-1h/muopt-sin-1h_stats_history.csv'
# muopt_w5s_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-w5s-sin-1h/muopt-w5s-sin-1h_stats_history.csv'
# muopt_w1s_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/muopt-1s-1h/muopt-1s-1h_stats_history.csv'
#
# compare_3autoscalers(muopt_stats_history, muopt_w5s_stats_history, muopt_w1s_stats_history,
#                      'muOpt', 'muOpt - w5s', 'muOpt - w1s', 'Requests/s',
#                      'muOpt15s-5s-1s-rps.pdf')
#
# muopt_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-sin-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# muopt_w5s_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-w5s-sin-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# muopt_w1s_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/muopt-1s-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
#
# compare_3autoscalers(muopt_replicas, muopt_w5s_replicas, muopt_w1s_replicas, 'muOpt',
#                      'muOpt - w5s', 'muOpt - w1s', 'Replicas', 'muOpt15s-5s-1s-replicas.pdf')
#
# muopt_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-sin-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# muopt_w5s_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-w5s-sin-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# muopt_w1s_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/muopt-1s-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# compare_3autoscalers(muopt_usage, muopt_w5s_usage, muopt_w1s_usage, 'muOpt', 'muOpt - w5s',
#                      'muOpt - w1s', 'Usage', 'muOpt15s-5s-1s-usage.pdf')
#
# # Comparison between muOpt (1s) and HPA
#
# hpa_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/hpa-sin-1h/hpa-sin-1h_stats_history.csv'
# hpa_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/hpa-sin-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# hpa_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/hpa-sin-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# hpa_w300 = [hpa_stats_history, hpa_replicas, hpa_usage]
#
# compare_2autoscalers(muopt_w1s_stats_history, hpa_stats_history, 'muOpt - w1s', 'HPA', 'Requests/s',
#                      'muOpt1s-HPA-rps.pdf')
# compare_2autoscalers(muopt_w1s_replicas, hpa_replicas, 'muOpt - w1s', 'HPA', 'Replicas', 'muOpt1s-HPA-replicas.pdf')
# compare_2autoscalers(muopt_w1s_usage, hpa_usage, 'muOpt - w1s', 'HPA', 'Usage', 'muOpt1s-HPA-usage.pdf')
#
# hpa_w30_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w30-1h/hpa-w30-1h_stats_history.csv'
# hpa_w30_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w30-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# hpa_w30_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w30-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# hpa_w30 = [hpa_w30_stats_history, hpa_w30_replicas, hpa_w30_usage]
#
# hpa_w15_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w15-1h/hpa-w15-1h_stats_history.csv'
# hpa_w15_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w15-1h/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
# hpa_w15_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240426/hpa-w15-1h/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
#
# hpa_w15 = [hpa_w15_stats_history, hpa_w15_replicas, hpa_w15_usage]
#
# compare_3autoscalers(hpa_stats_history, hpa_w30_stats_history, hpa_w15_stats_history, 'HPA(w 300s)', 'HPA (w 30s)',
#                      'HPA (w 15s)', 'Requests/s',
#                      'HPA-w300-w30-w15-rps.pdf')
# compare_3autoscalers(hpa_replicas, hpa_w30_replicas, hpa_w15_replicas, 'HPA (w 300s)', 'HPA (w 30s)', 'HPA (w 15)',
#                      'Replicas',
#                      'HPA-w300-w30-w15-replicas.pdf')
# compare_3autoscalers(hpa_usage, hpa_w30_usage, hpa_w15_usage, 'HPA (w 300s)', 'HPA (w 30s)', 'HPA (w 15s)', 'Usage',
#                      'HPA-w300-w30-w15-usage.pdf')
#
# muopt_w15 = [muopt_stats_history, muopt_replicas, muopt_usage]
#
# compare_2autoscalers(muopt_stats_history, hpa_w15_stats_history, 'muOpt (15s)', 'HPA (15s)', 'Requests/s', 'muopt-hpa-w15-rps.pdf')
# compare_2autoscalers(muopt_replicas, hpa_w15_replicas, 'muOpt (15s)', 'HPA (15s)', 'Replicas', 'muopt-hpa-w15-replicas.pdf')
# compare_2autoscalers(muopt_usage, hpa_w15_usage, 'muOpt (15s)', 'HPA (15s)', 'Usage', 'muopt-hpa-w15-usage.pdf')
#
#
# muopt_servicetime = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/muopt-sin-1h/Service_Time_(ms)/Service_Time_(ms)_3.csv'
# hpa_servicetime = '/home/robb/PycharmProjects/locust-flask-test/results/20240425/hpa-sin-1h/Service_Time_(ms)/Service_Time_(ms)_3.csv'
#
# compare_2autoscalers(muopt_servicetime, hpa_servicetime, 'muOpt (15s)', 'HPA (300s)', 'Service Time', 'muopt-hpa-service_time.pdf')
#
# path = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-15min/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# data = pd.read_csv(path)
# column = data['Usage']  # [0:399]
# print(column.mean())

#
# # 20 users
# hpa_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
# hpa_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/HPA-15m_stats_history.csv'
# hpa_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/HPA-15m/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
#
# data = pd.read_csv(hpa_usage)
# column = data['Usage']
# mean_usage = column.mean()
#
# data = pd.read_csv(hpa_rps)
# column = data['Requests/s']
# mean_rps = column.mean()
#
# data = pd.read_csv(hpa_replicas)
# column = data['Replicas']
# mean_replicas = column.mean()
#
# print(mean_usage)
# print(mean_rps)
# print(mean_replicas)
#
# print(mean_usage / (mean_rps / mean_replicas))


# muopt_usage = '/home/robb/PycharmProjects/locust-flask-test/results/20240423/muopt-15min/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'


hpa_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240429/hpa-sin_p400-30min/hpa-sin_p400-30min_stats_history.csv'
muopt_stats_history = '/home/robb/PycharmProjects/locust-flask-test/results/20240429/muopt-w30-sin_p400-30min/muopt-w30-sin_p400-30min_stats_history.csv'

compare_2autoscalers(muopt_stats_history, hpa_stats_history, 'muOpt', 'HPA', 'Requests/s')

muopt_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240429/muopt-w30-sin_p400-30min/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
hpa_replicas = '/home/robb/PycharmProjects/locust-flask-test/results/20240429/hpa-sin_p400-30min/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'

compare_2autoscalers(muopt_replicas, hpa_replicas, 'muOpt', 'HPA', 'Replicas')