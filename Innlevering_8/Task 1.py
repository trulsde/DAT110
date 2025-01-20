import numpy as np
import matplotlib.pyplot as plt

def biased_estimator(points):
    return max(points)

def unbiased_estimator(points):
    return 2 * points.mean()

def theta_appx(theta, sample_size):
    repetitions = 10000
    estimators_b = np.zeros(repetitions)
    estimators_ub = np.zeros(repetitions)

    for s in range(repetitions):
        sample = np.random.uniform(0, theta, sample_size)

        biased = biased_estimator(sample)
        unbiased = unbiased_estimator(sample)
        estimators_b[s] = biased
        estimators_ub[s] = unbiased


    return (estimators_b.mean(), estimators_ub.mean())

th = 4
test = [theta_appx(th, 2**n) for n in range(2, 16)]
plt.figure(figsize=(5, 5))
plt.plot(range(2, 16), test)
plt.axhline(th, color='red')
plt.xlabel("Sample size (log2)")
plt.ylabel("Estimator value")
plt.legend(['Biased', 'Unbiased', 'Real Theta'])
plt.show()