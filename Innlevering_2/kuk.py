df_pct2 = pd.read_csv('simpsons1.csv')
overall_successA = df_pct2['successA'].sum() / df_pct2['totalA'].sum()
print(overall_successA)
overall_successB = df_pct2['successB'].sum() / df_pct2['totalB'].sum()
print(overall_successB)
overall_row = {'subCategory': 'Overall',
               'successA': 0,
               'totalA': 0,
               'successB': 0,
               'totalB': 0
              }
df_pct2.loc[len(df_pct2)] = overall_row
df_pct2['successA'] = df_pct2['successA'] / df_pct2['totalA']
df_pct2['successB'] = df_pct2['successB'] / df_pct2['totalB']
df_pct2.loc[len(df_pct2) - 1, 'successA'] = overall_successA
df_pct2.loc[len(df_pct2) - 1, 'successB'] = overall_successB
df_pct2['successA'] = df_pct2['successA'].round(2)
df_pct2['successB'] = df_pct2['successB'].round(2)
df_pct2 = df_pct2.drop(['Unnamed: 0', 'totalA', 'totalB'], axis=1)
df_pct2