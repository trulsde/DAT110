import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Task 1.1
n = 200
flavours = ["Chocolate", "Vanilla", "Strawberry", "Straciatella", "Lemon"]
probs_0 = [.4, .2, .2, .1, .1]
probs_A = [.375, .15, .175, .1, .2]
expectations_0 = [n * prob for prob in probs_0]
expectations_A = [n * prob for prob in probs_A]
print(expectations_0)
print(expectations_A)

samples_0 = np.random.choice(flavours, size=(10000, n), p=probs_0)
samples_A = np.random.choice(flavours, size=(10000, n), p=probs_A)

chi_values_0 = []
chi_values_A = []

for sample in samples_0:
    observations = np.array([np.sum(sample == flavour, axis=0) for flavour in flavours])
    chi_value = np.sum([(data[0] - data[1])**2 / data[1] for data in zip(observations, expectations_0)])
    chi_values_0.append(chi_value)

for sample in samples_A:
    observations = np.array([np.sum(sample == flavour, axis=0) for flavour in flavours])
    chi_value = np.sum([(data[0] - data[1])**2 / data[1] for data in zip(observations, expectations_A)])
    chi_values_A.append(chi_value)


df = len(flavours) - 1
x = np.linspace(0, 50, 1000)

print(np.mean(chi_values_0))
print(np.mean(chi_values_A))


plt.figure()
plt.hist(chi_values_0, density=True, bins=50, color='white', edgecolor='black')
plt.axvline(chi2.ppf(.95, df), linestyle='--', color='tomato')
plt.plot(x, chi2.pdf(x, df), color='hotpink')
plt.legend(["95-percentile", "Chi2-distribution", "Sampled distribution"])
plt.title("Sample from H0-hypothesis", fontweight='bold')
plt.show()

plt.figure()
plt.hist(chi_values_A, density=True, bins=50, color='white', edgecolor='black')
plt.plot(x, chi2.pdf(x, df), color='hotpink')
plt.title("Sample from HA-hypothesis", fontweight='bold')
plt.show()
# Task 1.3

actual_stats = [64, 24, 43, 29, 40]
chi_test_0 = np.sum([(data[0] - data[1]) / data[1] for data in zip(actual_stats, expectations_0)])
chi_test_A = np.sum([(data[0] - data[1]) / data[1] for data in zip(actual_stats, expectations_A)])


