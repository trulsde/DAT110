from std import WeightedStd
import statistics as st
import numpy as np

x = np.random.randn(100).tolist()
weights = np.random.exponential(1, 100).tolist()

s1 = WeightedStd(x, weights)
w_mean = s1.weighted_mean()
w_std = s1.standard_deviation()

np_mean = np.average(x, weights=weights)
np_std = st.stdev(x)

print(f"My computation of weighted mean: {w_mean}\nNumpy weighted mean: {np_mean}")
print(f"My computation of standard deviation: {w_std}\nNumpy standard deviation: {np_std}")