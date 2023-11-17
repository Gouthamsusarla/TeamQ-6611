import tkinter as tk
from tkinter import ttk
import random

class Metrics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        total = sum(self.data)
        return total / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        counts = {}
        for num in self.data:
            counts[num] = counts.get(num, 0) + 1
        mode = [k for k, v in counts.items() if v == max(counts.values())]
        return mode

    def variance(self):
        mean = self.mean()
        total = sum((num - mean) ** 2 for num in self.data)
        return total / len(self.data)

    def mean_absolute_deviation(self):
        mean = self.mean()
        total = sum(abs(num - mean) for num in self.data)
        return total / len(self.data)

    def standard_deviation(self):
        return self.sqrt(self.variance())

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

    def sqrt(self, num):
        guess = num / 2
        while abs(guess ** 2 - num) > 0.0001:
            guess = (guess + num / guess) / 2
        return guess

class MetricsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metrics Calculator")
        self.metrics = None
        self.generated_data = []
        self.valid_input = True  # Flag to check if the input is valid

        # Create and set up input entry
        self.input_label = tk.Label(root, text="Enter a number greater than or equal to 1000:", font=("Helvetica", 12))
        self.input_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10)
        self.input_entry = tk.Entry(root, font=("Helvetica", 12))
        self.input_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=10, ipady=5, sticky="ew")
        self.input_entry.bind("<Return>", lambda event: self.generate_data())

        # Create and set up button for generating random data
        self.generate_button = tk.Button(root, text="Generate Data", command=self.generate_data, font=("Helvetica", 12))
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipady=5, sticky="ew")

        # Create and set up listbox for displaying generated data
        self.data_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.MULTIPLE, font=("Courier", 10))
        self.data_listbox.grid(row=0, rowspan=3, column=2, pady=10, padx=10, sticky="ns")

        # Create scrollbar for data_listbox
        self.scrollbar = tk.Scrollbar(root, command=self.data_listbox.yview)
        self.scrollbar.grid(row=0, rowspan=3, column=3, pady=10, sticky="ns")
        self.data_listbox.config(yscrollcommand=self.scrollbar.set)

        # Create and set up button for copying data
        self.copy_button = tk.Button(root, text="Copy Data", command=self.copy_data, font=("Helvetica", 12))
        self.copy_button.grid(row=3, column=2, columnspan=2, pady=5, padx=10, ipady=5, sticky="ew")

        # Create and set up result box
        self.result_box = tk.Text(root, height=7, width=30, font=("Courier", 10))
        self.result_box.grid(row=4, column=0, columnspan=4, pady=5, padx=10, sticky="ns")

        # Create and set up buttons for each metric
        metrics = ["Mean", "Median", "Mode", "Mean Absolute Deviation", "Standard Deviation", "Min", "Max"]
        for i, metric in enumerate(metrics):
            button = ttk.Button(root, text=metric, command=lambda m=metric: self.calculate_and_display(m),
                                style="Metrics.TButton")
            column = i % 2
            button.grid(row=i // 2 + 5, column=column * 2, pady=5, padx=10, ipadx=10, ipady=5, sticky="ew")

    def generate_data(self):
        try:
            n = int(self.input_entry.get())
            if n < 1000:
                raise ValueError("Please enter a number greater than or equal to 1000.")
            data = [random.randint(0, 1000) for _ in range(n)]
            self.metrics = Metrics(data)
            self.generated_data.append(data)
            self.update_data_listbox(data)
            self.reset_result_box()
            self.valid_input = True  # Set input flag to True for valid input
        except ValueError as e:
            self.data_listbox.delete(0, tk.END)  # Clear existing items in the list box
            self.result_box.delete(1.0, tk.END)  # Clear existing results
            self.result_box.insert(tk.END, str(e))
            self.valid_input = False  # Set input flag to False for invalid input

    def calculate_and_display(self, metric):
        try:
            if self.metrics is not None and self.valid_input:  # Check if data has been generated and input is valid
                # Convert metric label to snake_case
                metric_method = metric.lower().replace(" ", "_")
                result = getattr(self.metrics, metric_method)()
                self.result_box.delete(1.0, tk.END)  # Clear existing results
                self.result_box.insert(tk.END, f"{metric}: {result}")
            elif not self.valid_input:
                self.result_box.delete(1.0, tk.END)  # Clear existing results
                self.result_box.insert(tk.END, "Please generate valid data first.")
            else:
                self.result_box.delete(1.0, tk.END)  # Clear existing results
                self.result_box.insert(tk.END, "Please generate data first.")
        except AttributeError:
            self.result_box.delete(1.0, tk.END)  # Clear existing results
            self.result_box.insert(tk.END, "Invalid metric or method.")

    def update_data_listbox(self, data):
        self.data_listbox.delete(0, tk.END)  # Clear existing items
        formatted_data = ", ".join(map(str, data))
        split_data = formatted_data.split(", ")
        lines = [", ".join(split_data[i:i + 10]) for i in range(0, len(split_data), 10)]
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                self.data_listbox.insert(tk.END, line + ", ")
            else:
                self.data_listbox.insert(tk.END, line)

    def copy_data(self):
        all_data = self.data_listbox.get(0, tk.END)
        clipboard_data = "".join(all_data)
        self.root.clipboard_clear()
        self.root.clipboard_append(clipboard_data)
        self.root.update()  # Required to update clipboard
        self.result_box.delete(1.0, tk.END)  # Clear existing results
        self.result_box.insert(tk.END, "Data copied to clipboard.")

    def reset_result_box(self):
        self.result_box.delete(1.0, tk.END)  # Clear existing results

if __name__ == "__main__":
    root = tk.Tk()
    app = MetricsGUI(root)
    root.mainloop()
