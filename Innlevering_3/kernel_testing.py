import numpy as np
from Kernel import kernel

x = 4
h_values = [0.2, 0.1, 2]
xi = np.random.normal(0, 1, 25)

kernel = kernel(x, h_values, xi)
kernel.function()