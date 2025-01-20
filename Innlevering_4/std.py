class WeightedStd:
    def __init__(self, data: list, weights=None):
        self._data = data
        self.check_data()
        self._weights = weights
        self.check_weights()
        self.normalise_weights()
    def check_data(self):
        for value in self._data:
            assert isinstance(value, (int, float)), "All points in dataset must be of type int or float"
    def make_weights(self):
        weights = []
        for i in range(len(self._data)):
            weights.append(1)

        total = sum(weights)
        for i in range(len(weights)):
            weights[i] = weights[i] / total

        self._weights = weights

    def check_weights(self):
        if self._weights is None:
            self.make_weights()

        assert isinstance(self._weights, list), "Input of weights must be a list"
        for weight in self._weights:
            assert isinstance(weight, (int, float)), f"List of weights can only contain instances of type int or float. Got{type(weight)}"
            assert weight > 0, "Weights can't be negative"

    def normalise_weights(self):
        weights = self._weights
        if round(sum(weights), 0) != 1:
            sum_of_all_weights = sum(weights)
            for i in range(len(weights)):
                weights[i] = weights[i] / sum_of_all_weights

        return weights

    def weighted_mean(self):
        assert len(self._weights) == len(self._data), "Amount of weights must be equal to amount of datapoints"
        weighted_mean = 0
        for x in range(len(self._data)):
            weighted_mean += self._data[x] * self._weights[x]
        return weighted_mean

    def standard_deviation(self):
        n = len(self._data)
        std = 0
        sample_mean = sum(self._data) / n
        for xi in self._data:
            std += (xi - sample_mean)**2 / (n - 1)

        return std
