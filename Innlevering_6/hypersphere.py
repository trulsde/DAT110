import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

def radius_check(data):
    return np.linalg.norm(data, axis=1) # Must have axis=1 to calculate the norm of every row vector (data point) in 'points'.

sample_dict = {}
gamma_dict = {}

def gamma_volume(r, n):

    return (np.pi**(n/2) / gamma(n/2 + 1)) * r**n

for n in range(1, 11):
    no_of_points = 1000000

    points = np.random.uniform(-1, 1, size=(no_of_points, n))
    point_radia = radius_check(points)
    radia_within = point_radia[point_radia <= 1]

    sample_dict[n] = len(radia_within) / no_of_points
    gamma_dict[n] = gamma_volume(1, n)

plt.figure(figsize=(10, 10))
plt.plot(sample_dict.keys(), sample_dict.values(), color='coral')
plt.plot(gamma_dict.keys(), gamma_dict.values(), color='lightskyblue')
plt.legend(['Sample volume', 'Gamma function volume'])
plt.xlabel('Dimensions')
plt.ylabel('Volume')
plt.title('Volume of hypersphere calculated with 10^6 samples vs formula')
plt.savefig('hypersphere_1e6.jpg')
plt.show()

for n in range(1, 11):
    no_of_points = 1000

    points = np.random.uniform(-1, 1, size=(no_of_points, n))
    point_radia = radius_check(points)
    radia_within = point_radia[point_radia <= 1]

    sample_dict[n] = len(radia_within) / no_of_points
    gamma_dict[n] = gamma_volume(1, n)

plt.figure(figsize=(10, 10))
plt.plot(sample_dict.keys(), sample_dict.values(), color='coral')
plt.plot(gamma_dict.keys(), gamma_dict.values(), color='lightskyblue')
plt.legend(['Sample volume', 'Gamma function volume'])
plt.xlabel('Dimensions')
plt.ylabel('Volume')
plt.title('Volume of hypersphere calculated with 10^3 samples vs formula')
plt.savefig('hypersphere_1e3.jpg')
plt.show()

