import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd
from Histogram import Histogram as hi
import os


string_list = ["Fitte", "Satan", "Anarki", "Kommando", "Kommando", "Satan"]
int_list = [1, 6, 13, 29, 3, 6, 9]
mix_list = ["neiass", "boom", 6, 8]
not_list = 54

histogram1 = hi(string_list)
histogram2 = hi(int_list, 3)
#histogram3 = hi(mix_list, 6)
#histogram4 = hi(not_list, 5)

for i in range(5):
    normal_distribution_25 = rd.normal(0, 1, 25)
    my_histogram = hi(normal_distribution_25)
    np_histogram = np.histogram(normal_distribution_25)
    print('\nMe: ')
    my_histogram.plot()
    print('\nNumpy: ', np_histogram)

def plot_saver():

    dir_name = 'Plots'
    os.mkdir(dir_name)

    sample_sizes = [25, 100, 1000]
    bin_sizes = [10, 50, 100]

    for size in sample_sizes:
        fig, axs = plt.subplots(1, 3, figsize=(10, 5))
        sample = rd.normal(0, 1, size)
        axs = axs.flatten()
        for j, bins in enumerate(bin_sizes):
            ax = axs[j]
            ax.hist(sample, bins=bins, color='blue', edgecolor='black')
            ax.set_title(f'Samples: {len(sample)}, Bins: {bins}')
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')

        filename=f'Plots/hist_samplesize_{size}.jpg'
        plt.savefig(filename)
        plt.show()

plot_saver()




