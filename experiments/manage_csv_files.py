import pandas as pd
import re
import glob


def reformat_csv(in_path, value_name):  # , out_path):
    df = pd.read_csv(in_path, skiprows=1)
    df.columns = ['time', value_name]
    df['time'] = df['time'].apply(lambda x: reformat_time(x))
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    df = df.resample('1min').ffill()
    df.to_csv(in_path)  # out_path)



# Use ISO 8601 time format
def reformat_time(old_time):
    return pd.to_datetime(re.sub(r'\([^)]*\)', '', old_time))


for n_users in range(2, 18, 2):
    #n_users = 2

    experiment_name = "u" + str(n_users)
    print(experiment_name)
    folder_names = ['SpringTestApp_3Tier_-_Cores_per_replica', 'SpringTestApp_3Tier_-_CPU_Usage',
                    'SpringTestApp_3Tier_-_Response_Time', 'SpringTestApp_3Tier_-_RPS']
    print(folder_names)

    for folder_name in folder_names:
        folder_path = f"./data/20240404_exp5min_u2-16/{experiment_name}/{folder_name}"
        print(folder_path)
        pattern = "*.csv"
        files = glob.glob(f"{folder_path}/{pattern}")
        for file in files:
            reformat_csv(file, folder_name)

    # in_path = folder_path + "/SpringTestApp_3Tier_-_CPU_Usage_1.csv"
# out_path = experiment_folder + "u2_CPU_Usage/u2_CPU_Usage_1.csv"

# reformat_csv(in_path)  # ), out_path)
