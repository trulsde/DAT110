import scipy.integrate as integrate
import numpy as np
import math

inf = float('inf')

def z_score(value, mean, std):

    return (value - mean) / std

def cdf(a, b):

    return integrate.quad(lambda x: (1 / math.sqrt(2 * math.pi) * math.exp(-x**2 / 2)), a, b)

mean = 72.6
std = 4.78


# 4.1
z_score_80 = z_score(80, mean, std)
below_80 = cdf(-inf, z_score_80)[0]
print("Below 80:", below_80)

# 4.2
z_score_60 = z_score(60, mean, std)
below_60 = cdf(-inf, z_score_60)[0]
print("Below 60:", below_60)
between_60_and_80 = below_80 - below_60
print(between_60_and_80)

# 4.3
closest_to_5_check = 1
closest_value = 0
range = np.linspace(80, 80.5, 100)
for i in range:
    z = z_score(i, mean, std)
    percentage = cdf(-inf, z)[0]
    check = abs(percentage - 0.95)
    print(check, i, percentage)
    if check < closest_to_5_check:
        closest_to_5_check = check
        closest_value = i
        print(i)

print(f'Fastest 5% of vehivles drive faster than {closest_value} mph')
# Fastest 5% of vehicles drive faster than 80.46464 mph (or faster that appx 80.5 mph)

# 4.4
z_score_70 = z_score(70, mean, std)
below_70 = cdf(-inf, z_score_70)[0]
print(f"{below_70 * 100:.2f}% drive slower than or on the speed of mean")

# 4.5
print(f"P(5 cars <= 70 mph) = P(X <= 70)**5 = {below_70**5 * 100:.2f}%")