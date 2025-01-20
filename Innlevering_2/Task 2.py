import pandas as pd
import random as rd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv("SN_list_large.csv", header=0))
df = df.drop(columns=['SN Position'])
types = ['Ia', 'II', 'IIn']
df = df[df['Type'].isin(types)]
df['Date'] = pd.to_datetime(df['Date'])
years = sorted(df['Date'].unique())
print(years)

print(df.head(10))

