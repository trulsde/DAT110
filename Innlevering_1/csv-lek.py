import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_supernova = pd.DataFrame(pd.read_csv("SN_list-1.csv", header=0))

x = df_supernova['Type'].unique()
y = df_supernova['Type'].value_counts()

print(df_supernova['Date'].min(), df_supernova['Date'].max())


plt.bar(x, y, color="grey", edgecolor="black", linewidth=1)
for value in range(len(x)):
    plt.text(value - 0.2, y.iloc[value] + 0.5, f'{y.iloc[value]}')
plt.xlabel("Supernova Types")
plt.ylabel("Observations")
plt.title(
    f"Observations of supernova types\n"
    f"{df_supernova['Date'].min()} - {df_supernova['Date'].max()}",
    fontweight="bold")
plt.show()






