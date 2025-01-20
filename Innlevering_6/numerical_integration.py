import numpy as np

# Oppgave 3.1:
def numerical_integration(function, left, right, no_of_bars):
    span = np.linspace(left, right, no_of_bars)
    integral = 0
    for i in range(len(span)-1):
        box = function(span[i]) * (span[i+1] - span[i])
        integral += box

    return integral

# Oppgave 3.2:
def square(x):
    return x**2

def polynomial(x):
    return 3 * x**3 + 0.3 * x**2 + 4*x

def integral_square(left, right):
    def integral(x):
        return (1/3) * x**3
    return integral(right) - integral(left)

def integral_polynomial(left, right):
    def integral(x):
        return (3/4) * x**4 + 0.1 * x**3 - 2 * x**2

    return integral(right) - integral(left)

print("Polynomial function (3/4) * x**4 + 0.1 * x**3 - 2 * x**2 (bins / value): \n")
dict = {}
for i in range(1000, 100000, 10000):
    dict[i] = numerical_integration(polynomial, 6, 20, i)
print(f'{dict}\n')
print("Square function x**2 (bins / value): \n")
dict = {}
for i in range(1000, 100000, 10000):
    dict[i] = numerical_integration(square, 1, 13, i)
print(f'{dict}\n')

print('Calculated integrals: ')
print(integral_square(1, 13))
print(integral_polynomial(6, 20))

"""The polynomial function is a little off. Maybe it has to do with it having multiple local extremal points, so that the bins
will switch between exceeding the function graph and staying below?"""

# Oppgave 3.3:
print("\nOppgave 3.3")
def uniform(x, left, right, value):
    if x >= left and x <= right:
        return value
    else:
        return 0

def uniform_0_1(x):
    return uniform(x, 0, 1, 1)

print("Numerical integration of uniform distribution with 10 bins: ")
print(numerical_integration(uniform_0_1, -1, 12, 100))


