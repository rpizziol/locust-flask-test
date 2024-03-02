import pandas as pd
import numpy as np

input_csv_file = 'zipkin-traces_r1-u1.csv'
df = pd.read_csv(input_csv_file)
df['endtime'] = df['timestamp'] + df['duration']

# Leave only the endtime column
df = df.iloc[:, 5:]

df['endtime'] = np.floor(df['endtime'] / 60_000_000)

print(df)
