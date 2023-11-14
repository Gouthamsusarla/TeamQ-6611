# metrics/metrics.py
import random

class Metrics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        total = 0
        for num in self.data:
            total += num
        return total / len(self.data) # Calculate mean

    def median(self):
        sorted_data = self.bubble_sort(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 # Median is average of middle two numbers
        else:
            return sorted_data[n//2] # Median is middle number

    def mode(self):
        counts = {}
        for num in self.data:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        mode = []
        max_count = 0
        for num, count in counts.items():
            if count > max_count:
                mode = [num]
                max_count = count
            elif count == max_count:
                mode.append(num)
        return mode # Most common numbers

    def variance(self):
        mean = self.mean()
        total = 0
        for num in self.data:
            total += (num - mean) ** 2
        return total / len(self.data) # Average squared difference from mean

    def mean_absolute_deviation(self):
        mean = self.mean()
        total = 0
        for num in self.data:
            total += abs(num - mean)
        return total / len(self.data) # Average absolute difference from mean

    def standard_deviation(self):
        mean = self.mean()
        total = 0
        for num in self.data:
            total += (num - mean) ** 2
        variance = total / len(self.data)
        return self.sqrt(variance) # Square root of variance

    def min(self):
        min_val = self.data[0]
        for num in self.data:
            if num < min_val:
                min_val = num
        return min_val # Smallest number

    def max(self):
        max_val = self.data[0]
        for num in self.data:
            if num > max_val:
                max_val = num
        return max_val # Largest number

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data # Sort list using bubble sort

    def sqrt(self, num):
        guess = num / 2
        while abs(guess ** 2 - num) > 0.0001:
            guess = (guess + num / guess) / 2
        return guess # Calculate square root

# Generate n random integers between 0 and 1000
n = int(input("Enter a number greater than 1000: "))
data = [random.randint(0, 1000) for _ in range(n)]

# Create Metrics object and calculate statistics
metrics = Metrics(data)

#Print Mean
print(f"Mean: {metrics.mean()}")

#Print Median
print(f"Median: {metrics.median()}")

#Print Mode
print(f"Mode: {metrics.mode()}")

#Print Variance
print(f"Variance: {metrics.variance()}")

#Print Mean Absolute Deviation
print(f"Mean Absolute Deviation: {metrics.mean_absolute_deviation()}")

#Print Standard Deviation
print(f"Standard Deviation: {metrics.standard_deviation()}")

#Print Min
print(f"Min: {metrics.min()}")

#Print Max
print(f"Max: {metrics.max()}")