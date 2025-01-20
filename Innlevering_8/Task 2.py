from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 100
p_0 = 0.5
trials = np.arange(0, n+1)

pmf_values = binom.pmf(trials, n, p_0)
cdf_values = binom.cdf(trials, n, p_0)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(pmf_values)
ax[0].set_title('Probability mass function')
ax[0].set_ylabel('p', rotation=0, fontweight='bold')
ax[0].set_xlabel('No. of successes', fontweight='bold')
ax[1].plot(cdf_values)
ax[1].set_title('Cumulative density function')
ax[1].set_ylabel('p', rotation=0, fontweight='bold')
ax[1].set_xlabel('No. of successes', fontweight='bold')
ax[1].axvline(35, color='black', linestyle='--')
ax[1].legend(['CDF', 'x = 35'])
plt.show()

print(f'P-value of 35 successes out of n = 100 trials: {cdf_values[35]:.5f}')