# main.py
from metrics.metrics import generate_random_data, test_metrics
from ui.app import window

# Testing Metrics with random data
data = generate_random_data(1000)
test_metrics(data)