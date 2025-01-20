import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

probs_A = [.375, .15, .175, .1, .2]
expectations_A = [n * prob for prob in probs_A]

chi_values_A = []
for sample in samples_0:
    observations = np.array([np.sum(sample == flavour, axis=0) for flavour in flavours])
    chi_value = np.sum([(data[0] - data[1])**2 / data[1] for data in zip(observations, expectations_A)])
    chi_values_A.append(chi_value)