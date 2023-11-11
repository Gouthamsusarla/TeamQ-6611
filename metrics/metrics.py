# metrics/metrics.py
import random

class Metrics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        if not self.data:
            return None
        total = sum(self.data)
        return total / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        if not self.data:
            return None
        count_dict = {}
        for val in self.data:
            if val in count_dict:
                count_dict[val] += 1
            else:
                count_dict[val] = 1
        mode = [key for key, value in count_dict.items() if value == max(count_dict.values())]
        return mode

    def standard_deviation(self):
        if not self.data:
            return None
        mean = self.mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diff) / len(self.data)
        return variance**0.5

def generate_random_data(size):
    # Create a list of random integers within range
    return [random.randint(0, 1000) for _ in range(size)]

def test_metrics(data):
    # Create metrics object with data
    metrics = Metrics(data)

    # Print mean
    print("Mean:", metrics.mean())

    # Print median
    print("Median:", metrics.median())

    # Print mode
    print("Mode:", metrics.mode())

    # Print standard deviation
    print("Standard Deviation:", metrics.standard_deviation())