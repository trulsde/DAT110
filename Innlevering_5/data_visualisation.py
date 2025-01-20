import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

data = pd.read_csv("forest_properties.csv", header=1, sep=';')

data = data.drop(index=1)

df = pd.DataFrame(data)
df = df.rename({'Unnamed: 0': 'Size'}, axis=1)
total = df.iloc[0].tolist()
df = df.drop(index=0).reset_index(drop=True)
columns_with_ints = ['Productive forest area', 'Number of properties']
for column in columns_with_ints:
    df[column] = [int(value.replace(' ', '')) for value in df[column].tolist()]
def chart_plotter():

    fig, ax = plt.subplots(2, 2, figsize=(70, 40))
    for column in columns_with_ints:
        size_list = df['Size'].tolist()
        range = re.compile(r'\d*\s*\d+-*\d*\s*\d+')
        sizes = []
        for size in size_list:
            match = re.findall(range, size)
            if '-' not in match[0]:
                sizes.append(match[0] + ' +')
            else:
                sizes.append(match[0])


        ax[columns_with_ints.index(column)][0].pie(df[column], labels=sizes)
        ax[columns_with_ints.index(column)][0].set_title(column)
        ax[columns_with_ints.index(column)][1].bar(sizes, df[column])
        ax[columns_with_ints.index(column)][1].tick_params(axis='x', rotation=45)
        ax[columns_with_ints.index(column)][1].set_xlabel('Property size (decares)')
        ax[columns_with_ints.index(column)][1].set_ylabel('Area covered')
    plt.show()

def histogram_plotter():
    fig, ax = plt.subplots(1, 2, figsize=(70, 40))
    for i, column in enumerate(columns_with_ints):
        size_list = df['Size'].tolist()
        range = re.compile(r'\d*\s*\d+-*\d*\s*\d+')
        sizes = []
        for size in size_list:
            match = re.findall(range, size)
            if '-' not in match[0]:
                sizes.append(match[0] + ' +')
            else:
                sizes.append(match[0])

        bin_edges = [100, 250, 500, 1000, 2000, 5000, 20000, np.inf]  # Define your bin edges
        bin_labels = sizes

        # Plot histogram
        ax[i].hist(df[column], bins=bin_edges, align='left', rwidth=0.8, alpha=0.7, label='Histogram')
        ax[i].set_xlabel('Property size (decares)')
        ax[i].set_ylabel('Count')
        ax[i].set_title(f'Histogram of {column}')
        ax[i].set_xticks(bin_edges[:-1])
        ax[i].set_xticklabels(bin_labels, rotation=45)

        # Plot cumulative distribution
        cumulative_sum = np.cumsum(df[column])
        ax2 = ax[i].twinx()
        ax2.plot(bin_edges[:-1], cumulative_sum, marker='o', linestyle='-', color='r', label='Cumulative Distribution')
        ax2.set_ylabel('Cumulative Distribution', color='r')

    print(df)

# Dette plottet ble ganske stygt, men jeg har ikke tid til å jobbe mer med det...
chart_plotter()

# histogram_plotter(), denne fikk jeg dessverre ikke til å funke... De siste 15 linjene av denne prosedyren er
# ChatGPT som heller ikke klarer å hjelpe til...




