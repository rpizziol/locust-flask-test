from utils import convert_mat_to_csv, generate_sin_csv, plot_csv

# convert_mat_to_csv('./trace.mat', './trace.csv')


generate_sin_csv('./sin.csv', 10, 900, 0, 5, 1000)

plot_csv('./sin.csv')
# plot_csv('./workloads/trace.csv')
