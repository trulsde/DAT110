import math
import numpy


class Histogram:

    def __init__(self, list_of_data, number_of_bins=None, start=None, end=None):
        self._data = list_of_data
        self._number_of_bins = number_of_bins
        self._bin_values = {}
        self._startvalue = start
        self._endvalue = end
        self.check_list_and_bins(self._data)


    def check_list_and_bins(self, list_of_data):
        assert isinstance(list_of_data, (list, numpy.ndarray)), "Histogram class must take a list as parameter"
        for item in list_of_data:
            if isinstance(list_of_data[0], str):
                assert isinstance(item, type(list_of_data[0])), "This histogram class doesn't do lists with both strings and numbers. Please provide a list with either str types or int/float"
            else:
                assert isinstance(item, (int, float)), "This histogram class doesn't do lists with both strings and numbers. Please provide a list with either str types or int/float"

        if isinstance(list_of_data[0], str):
            self.string_values()
        else:
            self.numeric_values()

    def string_values(self):
        if self._number_of_bins != len(set(self._data)) and self._number_of_bins is not None:
            print(
                '------ Cannot operate with number of bins not equal to amount of unique list elements in string list.'
                ' Number of bins has been set to number of unique elements in list ------')
        self._number_of_bins = len(set(self._data))
        for item in self._data:
            if item in self._bin_values:
                pass
            self._bin_values[item] = self._data.count(item)
        assert len(self._bin_values) == self._number_of_bins, "self._number_of_bins does not match real amount of bins"

    def numeric_values(self):
        if self._number_of_bins is None:
            self._number_of_bins = math.floor(math.sqrt(len(self._data)))
        if self._startvalue is None:
            self._startvalue = min(self._data)
        if self._endvalue is None:
            self._endvalue = max(self._data)

        value_range = self._endvalue - self._startvalue
        bin_width = value_range / self._number_of_bins

        for bins in range(self._number_of_bins):
            bin_start = self._startvalue + bins * bin_width
            bin_end = bin_start + bin_width
            count = sum(bin_start <= value < bin_end for value in self._data)
            self._bin_values[f'{bin_start} - {bin_end}'] = count


    def get_data(self):
        return self._data

    def get_bin_values(self):
        return self._bin_values

    def plot(self):
        longest_label_length = max(len(key) for key in self._bin_values)

        for key in self._bin_values:
            space = ' ' * (longest_label_length - len(key))
            print(f'{key}', space, '|', '*' * self._bin_values[key])