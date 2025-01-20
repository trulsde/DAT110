import numpy as np
import scipy.stats as stats
import matplotlib . pyplot as plt

n = 30
offset = [0, 0.5, -0.8, 0., 0.]

x = []
for i in range(len(offset)):
    thing = np.random.randn(n) + (offset[i])
    x.append(thing)
    print(thing)

# Task 2.2
sample_means = [i.mean() for i in x]
sample_var = [i.std()**2 for i in x]

# Task 2.3

# total number of groups k:
k = len(x)
# number of observations for each group
ni = [len(sample) for sample in x]
# total number of observations n:
n = np.sum(ni)
# mean outcome of all groups
x_mean = np.sum([sample_means]).mean()
# df's
df_G = 1 / (1 - k)
df_E = n - k
# sum of squares between groups
SSG = np.sum([n * (x - x_mean)**2 for n, x in zip(ni, sample_means)])

# sum of squared errors
SSE = np.sum([(n - 1) * var for n, var in zip(ni, sample_var)])
# mean squared error
MSE = SSE / df_E
MSG = SSG / df_G
print(f"MSE: {MSE}, MSG: {MSG}")
