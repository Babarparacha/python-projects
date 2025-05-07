import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function: Convert Date to Timestamp
def date_to_timestamp():
    date_str = date_entry.get()
    try:
        dt = datetime.strptime(date_str, "%d-%m-%Y-%H:%M:%S")
        timestamp = int(dt.timestamp())
        date_result_var.set(f"Timestamp: {timestamp}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please use format: DD-MM-YYYY-HH:MM:SS")

# Function: Convert Timestamp to Date
def timestamp_to_date():
    ts_str = timestamp_entry.get()
    try:
        ts = int(ts_str)
        dt = datetime.fromtimestamp(ts)
        timestamp_result_var.set(f"Date: {dt.strftime('%d-%m-%Y %H:%M:%S')}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer timestamp.")

# Create GUI window
root = tk.Tk()
root.title("Date ↔ Timestamp Converter")

# Variables for results
date_result_var = tk.StringVar()
timestamp_result_var = tk.StringVar()

# --- Date to Timestamp UI ---
tk.Label(root, text="Enter Date (DD-MM-YYYY-HH:MM:SS):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
date_entry = tk.Entry(root, width=30)
date_entry.grid(row=0, column=1, padx=10)
tk.Button(root, text="Convert to Timestamp", command=date_to_timestamp).grid(row=0, column=2, padx=10)
tk.Label(root, textvariable=date_result_var, fg="blue").grid(row=1, column=1, columnspan=2, sticky="w", padx=10)

# --- Timestamp to Date UI ---
tk.Label(root, text="Enter Timestamp:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
timestamp_entry = tk.Entry(root, width=30)
timestamp_entry.grid(row=2, column=1, padx=10)
tk.Button(root, text="Convert to Date", command=timestamp_to_date).grid(row=2, column=2, padx=10)
tk.Label(root, textvariable=timestamp_result_var, fg="green").grid(row=3, column=1, columnspan=2, sticky="w", padx=10)

# Run the app
root.mainloop()
