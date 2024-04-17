import pandas as pd


def calculate_average_df(filename):
    df = pd.read_csv(filename)
    df_padding = int(df.shape[0] / 8)
    return df.iloc[df_padding:-df_padding, 1].mean()
    # return df.iloc[:, 1].mean()


def calculate_service_time(cpu_filename, rps_filename):
    # Calculate average CPU usage
    avg_cpu = calculate_average_df(cpu_filename)  # / 2
    # print(avg_cpu)

    # Calculate average RPS
    avg_rps = calculate_average_df(rps_filename)
    # print(avg_rps)

    # Calculate average service time
    return avg_cpu / avg_rps


#

# folder_name = './data/20240409_5min_u2/u2'
#
#
# avg_st = calculate_service_time(f'{folder_name}/SpringTestApp_3Tier_-_CPU_Usage.csv', f'{folder_name}/SpringTestApp_3Tier_-_RPS.csv')
# print(f"Average Service Time of Tier 3: {avg_st * 1000} ms")

folder_name = './data/20240410_u2-32'

for n_users in range(2, 34, 2):
    experiment_name = f"u{n_users}"
    print(f"Experiment with {n_users} users.")
    for tier in range(1, 4):
        rps_filename = f'{folder_name}/{experiment_name}/SpringTestApp_3Tier_-_RPS/SpringTestApp_3Tier_-_RPS_{tier}.csv'
        avg_st = calculate_service_time(
            f'{folder_name}/{experiment_name}/SpringTestApp_3Tier_-_CPU_Usage/SpringTestApp_3Tier_-_CPU_Usage_{tier}.csv',
            rps_filename
        )
        avg_rps = calculate_average_df(rps_filename)
        print(f"Average Service Time of Tier {tier}: {avg_st * 1000} ms - {avg_rps} rps")
