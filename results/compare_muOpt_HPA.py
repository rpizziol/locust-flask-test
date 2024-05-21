import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_numpyarray(filename, index):
    df = pd.read_csv(filename)
    column = df[index]
    return column.to_numpy()


def increment(value1, value2):
    if value2 == 0:
        return 'NaN'
    else:
        incr = round(((value1 - value2) / value2) * 100, 2)
        if incr >= 0:
            return f'+{incr}'
        else:
            return f'{incr}'


def print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt, date_pdf,
                           usage_level):
    hpa_folder = f'/home/robb/PycharmProjects/locust-flask-test/results/{date_hpa}/{hpa_experiment_name}'
    muopt_folder = f'/home/robb/PycharmProjects/locust-flask-test/results/{date_muopt}/{muopt_experiment_name}'
    hpa_rps = f'{hpa_folder}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_3.csv'
    hpa_replicas = f'{hpa_folder}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
    hpa_usage = f'{hpa_folder}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'

    hpa_rps_np = get_numpyarray(hpa_rps, 'RPS')
    hpa_replicas_np = get_numpyarray(hpa_replicas, 'Replicas')
    hpa_usage_np = get_numpyarray(hpa_usage, 'Usage')

    muopt_rps = f'{muopt_folder}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_3.csv'
    muopt_replicas = f'{muopt_folder}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
    muopt_usage = f'{muopt_folder}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'

    muopt_rps_np = get_numpyarray(muopt_rps, 'RPS')
    muopt_replicas_np = get_numpyarray(muopt_replicas, 'Replicas')
    muopt_usage_np = get_numpyarray(muopt_usage, 'Usage')

    print("RPS Integral Comparison")
    hpa_rps_int = np.trapz(hpa_rps_np)
    print(f"HPA = {round(hpa_rps_int, 2)} rps")
    muopt_rps_int = np.trapz(muopt_rps_np)
    print(f"muOpt = {round(muopt_rps_int, 2)} rps")
    print(f"Increment = {increment(muopt_rps_int, hpa_rps_int)}%\n")

    print("Replicas Integral Comparison")
    hpa_replicas_int = np.trapz(hpa_replicas_np)
    print(f"HPA = {round(hpa_replicas_int, 2)} replicas")
    muopt_replicas_int = np.trapz(muopt_replicas_np)
    print(f"muOpt = {round(muopt_replicas_int, 2)} replicas")
    print(f"Increment = {increment(muopt_replicas_int, hpa_replicas_int)}%\n")

    print("Average Usage Comparison")
    hpa_usage_int = np.mean(hpa_usage_np)
    print(f"HPA = {round(hpa_usage_int, 2)} CPU cores")
    muopt_usage_int = np.mean(muopt_usage_np)
    print(f"muOpt = {round(muopt_usage_int, 2)} CPU cores")
    print(f"Increment = {increment(muopt_usage_int, hpa_usage_int)}%\n")

    # Create the figure and subplots
    fig, axs = plt.subplots(3, 1)  # 3 rows, 1 column

    # Plot data on the second subplot
    axs[0].step(np.linspace(1, muopt_rps_np.size, muopt_rps_np.size), muopt_rps_np, label='muOpt RPS')
    axs[0].step(np.linspace(1, hpa_rps_np.size, hpa_rps_np.size), hpa_rps_np, label='HPA RPS')
    axs[0].set_title('RPS')
    axs[0].legend()

    axs[1].step(np.linspace(1, muopt_replicas_np.size, muopt_replicas_np.size), muopt_replicas_np,
                label='muOpt Replicas')
    axs[1].step(np.linspace(1, hpa_replicas_np.size, hpa_replicas_np.size), hpa_replicas_np, label='HPA Replicas')
    axs[1].set_title('Replicas')
    axs[1].legend()

    axs[2].step(np.linspace(1, muopt_usage_np.size, muopt_usage_np.size), muopt_usage_np, label='muOpt Usage')
    axs[2].step(np.linspace(1, hpa_usage_np.size, hpa_usage_np.size), hpa_usage_np, label='HPA Usage')
    axs[2].set_title('Usage')
    axs[2].axhline(y=usage_level, color='red', linestyle='--', linewidth=1)
    axs[2].legend()

    plt.savefig(f"./pdfs/{date_pdf}_{title}.pdf")
    plt.tight_layout()
    plt.show()

    # Errors comparison

    hpa_errors_file = f'{hpa_folder}/{hpa_experiment_name}_failures.csv'
    muopt_errors_file = f'{muopt_folder}/{muopt_experiment_name}_failures.csv'

    hpa_errors_df = pd.read_csv(hpa_errors_file)
    muopt_errors_df = pd.read_csv(muopt_errors_file)

    tot_hpa_errors = hpa_errors_df["Occurrences"].sum()
    tot_muopt_errors = muopt_errors_df["Occurrences"].sum()

    print('Errors Comparison')
    print(f'HPA = {tot_hpa_errors}')
    print(f'muOpt = {tot_muopt_errors}')
    print(f'Increment = {increment(tot_muopt_errors, tot_hpa_errors)}%\n')


# Sin p800, 2000s with readiness probe, 50ms service time
# date = '20240503'
# title = 'ReadinessProbe-sinp800-st50ms-2000s_muOpt_vs_HPA'
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240503/hpa-sin400-2-max140-st50ms-2000s-readiness-probe'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240503/muopt-sin400-2-max140-st50ms-2000s-readiness-probe'
# print_comparison_plots(hpa_folder, 'hpa-sin400-2-max140-st50ms-2000s-readiness-probe', muopt_folder,
#                        'muopt-sin400-2-max140-st50ms-2000s-readiness-probe', title, date)

# # Sin p400, 2000s with readiness probe, 50ms service time
# date = '20240504'
# title = 'ReadinessProbe-sinp400-st50ms-2000s-muOpt_vs_HPA'
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240504/hpa-sinp400-readinessprobe-50ms-2000s'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240504/muopt-sinp400-readinessprobe-50ms-2000s'
# print_comparison_plots(hpa_folder, 'hpa-sinp400-readinessprobe-50ms-2000s', muopt_folder,
#                        'muopt-sinp400-readinessprobe-50ms-2000s', title, date)

# # Sin p200 with long interruption, 2000s with readiness probe, 50ms service time
# date = '20240506'
# title = 'Sinp200-mid-st50ms-2000s-muOpt_vs_HPA'
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/hpa-sin_p200_mid'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/muopt-sin_p200_mid'
# print_comparison_plots(hpa_folder, 'hpa-sin_p200_mid', muopt_folder, 'muopt-sin_p200_mid', title, date)
#
# # Sin800, 2000s with readiness probe, 50ms service time
# date = '20240506'
# title = 'muOpt_vs_HPA_sin800'
# print(title)
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/hpa-sin800-1h'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/muopt-sin800-1h'
# print_comparison_plots(hpa_folder, 'hpa-sin800-1h', muopt_folder,
#                        'muopt-sin800-1h', title, date)
#
# # Sin400, 2000s with readiness probe, 50ms service time
# date = '20240506'
# title = 'muOpt_vs_HPA_sin400'
# print(title)
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/hpa-sin400-1h'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/muopt-sin400-1h'
# print_comparison_plots(hpa_folder, 'hpa-sin400-1h', muopt_folder,
#                        'muopt-sin400-1h', title, date)
#
#
# # Twitter Workload
# date = '20240506'
# title = 'muOpt_vs_HPA_Twitter'
# print(title)
# hpa_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/hpa-twitter-1h'
# muopt_folder = '/home/robb/PycharmProjects/locust-flask-test/results/20240506/muopt-twitter-1h'
# print_comparison_plots(hpa_folder, 'hpa-twitter-1h', muopt_folder,
#                        'muopt-twitter-1h', title, date)

# # 50 Users, 20 minutes, usage target 20
# title = 'muOpt_vs_HPA_u50-20m-usage20'
# date_hpa = '20240507'
# date_muopt = '20240507'
# hpa_experiment_name = 'u50-20m-hpa20'
# muopt_experiment_name = 'u50-20m-muopt20'
# print(title)
# print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt)
#
#
# # 50 Users, 20 minutes, usage target 80
# title = 'muOpt_vs_HPA_u50-20m-usage80'
# date_hpa = '20240507'
# date_muopt = '20240508'
# hpa_experiment_name = 'u50-20m-hpa80'
# muopt_experiment_name = 'u50-20m-muopt80'
# print(title)
# print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt)

#
# # 50 Users, 45 minutes, usage target 50
# title = 'u50-45m-usage50-muOpt_vs_HPA'
#
# date_hpa = '20240508'
# date_muopt = '20240508'
# hpa_experiment_name = 'u50-45m-hpa50'
# muopt_experiment_name = 'u50-45m-muopt50'
# print(title)
# print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt, '20240509')


#
# # 50 Users, 45 minutes, usage target 50
# title = 'u50-45m-usage20-muOpt_vs_HPA'
#
# date_hpa = '20240508'
# date_muopt = '20240509'
# hpa_experiment_name = 'u50-45m-hpa20'
# muopt_experiment_name = 'u50-45m-muopt20'
# print(title)
# print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt, '20240509')


# 50 Users, 45 minutes, usage target 80
title = 'u50-45m-usage80-muOpt_vs_HPA'

date_hpa = '20240508'
date_muopt = '20240509'
hpa_experiment_name = 'u50-45m-hpa80'
muopt_experiment_name = 'u50-45m-muopt80'
print(title)
print_comparison_plots(hpa_experiment_name, muopt_experiment_name, title, date_hpa, date_muopt, '20240509', 0.8)
