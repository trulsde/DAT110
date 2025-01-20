import math
import numpy as np
import matplotlib.pyplot as plt

class kernel:

    def __init__(self, x, h, dataset):
        self._x = x
        self._h_values = h
        self._data = dataset
        self.assertion()

    def assertion(self):
        assert isinstance(self._x, (int, float)), "Value x must be of type int or float"
        assert isinstance(self._data, np.ndarray), "Set of x data values must be an array"
        if isinstance(self._h_values, (list, tuple)):
            for i in self._h_values:
                assert isinstance(i, (int, float)), "h values must be numeric"
        elif isinstance(self._h_values, (int, float)):
            pass
        else:
            raise ValueError("h value must be numeric")

    def function(self):

        if isinstance(self._h_values, (list, tuple)):
            for h in self._h_values:
                y_values = []
                for xi in self._data:
                    y = 1 / (h * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((self._x - xi) / h)**2)
                    y_values.append(y)

                plt.plot(self._data, y_values, color='deepskyblue')
                plt.show()
        else:
            y_values = []
            for xi in self._data:
                y = 1 / (self._h_values * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((self._x - xi) / self._h_values) ** 2)
                y_values.append(y)

            plt.plot(self._data, y_values, color='deepskyblue')
            plt.show()
