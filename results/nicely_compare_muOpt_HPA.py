import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font_size = 15
legend_size = 13

results = '/home/robb/PycharmProjects/locust-flask-test/results'


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


def print_comparison(index, algorithm1, label1, algorithm2, label2):
    np1 = get_numpyarray(algorithm1, index)
    np2 = get_numpyarray(algorithm2, index)

    # # Integral Comparison
    # int1 = np.trapz(np1)
    # int2 = np.trapz(np2)
    #
    # print(f'-- Integral {index} comparison --')
    # print(f"{label1} = {round(int1, 2)}")
    # print(f"{label2} = {round(int2, 2)}")
    # print(f"   {increment(int1, int2)}%\n")

    # Average Value Comparison
    mean1 = np.mean(np1)
    mean2 = np.mean(np2)

    print(f'-- Average {index} comparison --')
    print(f"{label1} = {round(mean1, 2)}")
    print(f"{label2} = {round(mean2, 2)}")
    print(f"   {increment(mean1, mean2)}%\n")


def plot_workload(wl_path, pdf_filename):
    data = pd.read_csv(wl_path)
    column = data['User Count']
    plt.figure(figsize=(4, 3))
    plt.step(np.linspace(1, column.size, column.size), column, linestyle='-', label='Users')
    plt.title(f"Load Shape")
    plt.xlabel('Time (s)', fontsize=font_size)
    plt.ylabel('#Users', fontsize=font_size)
    plt.legend()  # loc='lower right'
    plt.grid()
    # plt.title(pdf_filename)
    plt.tight_layout()
    plt.savefig(f'{results}/pdfs/{pdf_filename}.pdf')
    plt.show()
    plt.close()


def plot_comparison(filename1, label1, filename2, label2, pdf_filename, index, x_label, y_label, usage_level=0.0,
                    max_value=0.0, filename3="", label3=""):
    plt.figure(figsize=(4, 3))

    # Muopt data
    data1 = pd.read_csv(filename1)
    column1 = data1[index]
    plt.step(np.linspace(1, column1.size, column1.size), column1, linestyle='-', label=label1,
             linewidth=2)

    # HPA data
    data2 = pd.read_csv(filename2)
    column2 = data2[index]
    plt.step(np.linspace(1, column2.size, column2.size), column2, linestyle='-', label=label2, linewidth=2)

    if filename3 != "" and label3 != "":
        data3 = pd.read_csv(filename3)
        column3 = data3[index]
        plt.step(np.linspace(1, column3.size, column3.size), column3, linestyle='-', label=label3, linewidth=2)

    plt.xlabel(x_label, fontsize=font_size)
    plt.ylabel(y_label, fontsize=font_size)
    plt.grid()

    if usage_level != 0.0:
        plt.axhline(y=usage_level, color='red', linestyle='--', linewidth=2, label='Target')
    if max_value != 0.0:
        plt.ylim(0, max_value)

    pdfs_path = '/home/robb/PycharmProjects/locust-flask-test/results/pdfs'

    plt.legend(fontsize=legend_size)  # loc='lower right'
    # plt.title(pdf_filename)
    plt.tight_layout()
    plt.savefig(f'{pdfs_path}/paper/{pdf_filename}.pdf')
    plt.show()
    plt.close()

    print_comparison(index, filename1, label1, filename2, label2)
    if filename3 != "" and label3 != "":
        print_comparison(index, filename3, label3, filename2, label2)


def generate_all_comparison_plots_by_experiment(exp_name, label1, date1, exp1, label2, date2, exp2, usage_level=0.5,
                                                label3="", date3="", exp3=""):
    print(f'--- {exp_name} ---')

    rps1 = f'{results}/{date1}/{exp1}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_4.csv'
    replicas1 = f'{results}/{date1}/{exp1}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
    cpu1 = f'{results}/{date1}/{exp1}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
    locust1 = f'{results}/{date1}/{exp1}/{exp1}_stats_history.csv'

    rps2 = f'{results}/{date2}/{exp2}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_4.csv'
    replicas2 = f'{results}/{date2}/{exp2}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
    cpu2 = f'{results}/{date2}/{exp2}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
    locust2 = f'{results}/{date2}/{exp2}/{exp2}_stats_history.csv'

    if label3 != "":
        rps3 = f'{results}/{date3}/{exp3}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_4.csv'
        replicas3 = f'{results}/{date3}/{exp3}/SpringTestApp_3Tier_-_Replicas/SpringTestApp_3Tier_-_Replicas_4.csv'
        cpu3 = f'{results}/{date3}/{exp3}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_4.csv'
        locust3 = f'{results}/{date3}/{exp3}/{exp3}_stats_history.csv'
    else:
        rps3 = ""
        replicas3 = ""
        cpu3 = ""
        locust3 = ""

    # muopt_locust = f'{results_path}/{muopt_date}/{muopt_exp}/{muopt_exp}_stats_history.csv'
    # hpa_locust = f'{results_path}/{hpa_date}/{hpa_exp}/{hpa_exp}_stats_history.csv'
    # plot_workload(muopt_locust, f'{exp_name}_wl')

    plot_comparison(rps1, label1, rps2, label2, f'{exp_name}_rps', 'RPS', 'Time (m)', 'Throughput (req/s)',
                    max_value=140, filename3=rps3, label3=label3)
    plot_comparison(replicas1, label1, replicas2, label2, f'{exp_name}_replicas', 'Replicas', 'Time (m)',
                    '#Cores', max_value=45, filename3=replicas3, label3=label3)
    plot_comparison(cpu1, label1, cpu2, label2, f'{exp_name}_cpu', 'Usage', 'Time (m)', 'CPU Usage (%)',
                    usage_level,
                    max_value=1, filename3=cpu3, label3=label3)
    plot_comparison(locust1, label1, locust2, label2, f'{exp_name}_errors', 'Total Failure Count', 'Time (s)', 'Errors',
                    filename3=locust3, label3=label3)

    plot_comparison(locust1, label1, locust2, label2, f'{exp_name}_rps_locust', "Requests/s", 'Time (s)',
                    'Throughput (req/s)',
                    max_value=140, filename3=locust3, label3=label3)

    # # # 50 users, target usage 20%, 20 minutes
    # # generate_all_comparison_plots_by_experiment('20240509_u50-20m-usage20', '20240507', 'u50-20m-muopt20', '20240507',
    # #                                             'u50-20m-hpa20', 0.2)
    # #
    #
    # # 50 users, target usage 50%, 45 minutes
    # generate_all_comparison_plots_by_experiment('u50-45m-usage50', '20240508', 'u50-45m-muopt50', '20240508',
    #                                             'u50-45m-hpa50', 0.5)
    #
    # # 50 users, target usage 50%, 45 minutes
    # generate_all_comparison_plots_by_experiment('u50-45m-usage20', '20240509', 'u50-45m-muopt20', '20240508',
    #                                             'u50-45m-hpa20', 0.2)
    #
    # # 50 users, target usage 50%, 45 minutes
    # generate_all_comparison_plots_by_experiment('u50-45m-usage80', '20240509', 'u50-45m-muopt80', '20240508',
    #                                             'u50-45m-hpa80', 0.8)
    # #
    # # # sin800, target usage 50%, 45 minutes
    # # generate_all_comparison_plots_by_experiment('sin800-45m-usage50_HPA_vs_muOpt', '20240509', 'sin800-45m-muopt50', '20240509',
    # #                                             'sin800-45m-hpa50', 0.5)
    # #
    # # # sin800, target usage 50%, 45 minutes (muopt prealloc)
    # # generate_all_comparison_plots_by_experiment('sin800-45m-usage50-HPA_vs_muOpt-prealloc', '20240509', 'sin800-45m-muopt50-prealloc', '20240509',
    # #                                             'sin800-45m-hpa50', 0.5)

    # # sin200, 70 min, muOpt vs HPA
    # generate_all_comparison_plots_by_experiment('sin200-60m-HPA_vs_muOpt', '20240510', 'sin200-70m-muopt', '20240510',
    #                                             'sin200-70m-hpa')
    # # sin400, 70 min, muOpt vs HPA
    # generate_all_comparison_plots_by_experiment('sin400-60m-HPA_vs_muOpt', '20240509', 'sin400-70m-muopt', '20240510',
    #                                             'sin400-70m-hpa')
    #
    # # sin800, 70 min, muOpt vs HPA
    # generate_all_comparison_plots_by_experiment('sin800-60m-HPA_vs_muOpt', '20240509', 'sin800-70m-muopt', '20240510',
    #                                             'sin800-70m-hpa')
    #
    #
    # # sin400, 70 min, muOpt vs HPA 15s
    # generate_all_comparison_plots_by_experiment('sin400-60m-HPA15w_vs_muOpt', '20240509', 'sin400-70m-muopt', '20240510',
    #                                             'sin400-70m-hpa15w')
    #
    # # sin400, 70 min, muOpt vs HPA 60s
    # generate_all_comparison_plots_by_experiment('sin400-60m-HPA60w_vs_muOpt', '20240509', 'sin400-70m-muopt', '20240510',
    #                                             'sin400-70m-hpa60w')

    # step2, 1h, muOpt vs HPA
    # generate_all_comparison_plots_by_experiment('step2-1h-HPA_vs_muOpt', '20240513', 'step2-1h-muopt', '20240513',
    #                                             'step2-1h-hpa')

    # sin200, 20min, muOpt with 2secs preStop vs muOpt
    # generate_all_comparison_plots_by_experiment('sin200-1200s-muOpt_vs_muOpt_preStop', 'muOpt - preStop (2 s)', '20240514',
    #                                             'sin200-1200s-muopt-testPreStop', 'muOpt', '20240514',
    #                                             'sin200-1200s-muopt-test', label3='muOpt - preStop (30 s)',
    #                                             exp3='sin200-1200s-muopt-testPreStop30s', date3='20240514')


# generate_all_comparison_plots_by_experiment('sin200-1200s-muOpt_vs_muOpt_preStop2', 'muOpt preStop2', '20240514',
#                                             'sin200-1200s-muopt-testPreStop2',
#                                             'muOpt', '20240514', 'sin200-1200s-muopt-test')
#
# generate_all_comparison_plots_by_experiment('sin200-1200s-muOpt_vs_muOpt_graceful', 'muOpt graceful', '20240515',
#                                             'sin200-1200s-muopt-graceful',
#                                             'muOpt', '20240514', 'sin200-1200s-muopt-test')

# generate_all_comparison_plots_by_experiment('sin200-1200s-muOpt_vs_muOpt_kub-api', 'muOpt kub-api', '20240517',
#                                             'sin200-1200s-muopt-kub-api',
#                                             'muOpt', '20240514', 'sin200-1200s-muopt-test')
#
# generate_all_comparison_plots_by_experiment('sin200-1200s-muOpt_graceful_vs_muOpt_kub-api', 'muOpt kub-api', '20240517',
#                                             'sin200-1200s-muopt-kub-api',
#                                             'muOpt graceful', '20240515', 'sin200-1200s-muopt-graceful')
#
# generate_all_comparison_plots_by_experiment('sin200-1h-VPA_vs_HPA',
#                                             'VPA', '20240520', 'sin200-1h-vpa',
#                                             'HPA', '20240510', 'sin200-70m-hpa' )


sin200_vpa_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240520/sin200-1h-vpa/RPS/RPS_4.csv'
sin200_hpa_rps = '/home/robb/PycharmProjects/locust-flask-test/results/20240510/sin200-70m-hpa/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_4.csv'


plot_comparison(sin200_vpa_rps, 'VPA', sin200_hpa_rps, 'HPA', f'sin200-1h-VPA_vs_HPA_rps', 'RPS', 'Time (m)', 'Throughput (req/s)',
                max_value=140)