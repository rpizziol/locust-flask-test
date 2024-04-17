from utils import convert_mat_to_csv, generate_sin_csv, plot_csv

# convert_mat_to_csv('./trace.mat', './trace.csv')


generate_sin_csv('./sin160.csv', 10, 160, 0, 1, 200)

plot_csv('./sin160.csv')
# plot_csv('./workloads/trace.csv')
