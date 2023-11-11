# ui/app.py
import tkinter as tk
from metrics.metrics import Metrics

def on_calculate():
    data = [int(val) for val in entry.get().split()]
    metrics = Metrics(data)
    result_label.config(text=f"Mean: {metrics.mean()}, Median: {metrics.median()}, Mode: {metrics.mode()}, Standard Deviation: {metrics.standard_deviation()}")

window = tk.Tk()
window.title("METRICS Calculator")

input_label = tk.Label(window, text="Enter space-separated data:")
entry = tk.Entry(window)
calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
result_label = tk.Label(window, text="")

input_label.pack()
entry.pack()
calculate_button.pack()
result_label.pack()

window.mainloop()
