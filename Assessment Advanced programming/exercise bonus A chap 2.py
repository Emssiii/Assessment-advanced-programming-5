"""
=======================================================
EXERCISE A: TEMPERATURE CONVERTER
=======================================================
A GUI application that implements a temperature 
converter using Tkinter, allowing users to convert 
between Celsius and Fahrenheit.
=======================================================
"""

import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

def clear_fields():
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Exercise A: Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), fg="#2c3e50")
title_label.pack(pady=10)

# Celsius to Fahrenheit section
celsius_frame = tk.Frame(root)
celsius_frame.pack(pady=10)

tk.Label(celsius_frame, text="Celsius:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
celsius_entry = tk.Entry(celsius_frame, width=15, font=("Arial", 11))
celsius_entry.grid(row=0, column=1, padx=5)
convert_to_f_btn = tk.Button(celsius_frame, text="Convert to °F", command=celsius_to_fahrenheit, 
                              bg="#3498db", fg="white", font=("Arial", 10))
convert_to_f_btn.grid(row=0, column=2, padx=5)

# Fahrenheit to Celsius section
fahrenheit_frame = tk.Frame(root)
fahrenheit_frame.pack(pady=10)

tk.Label(fahrenheit_frame, text="Fahrenheit:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
fahrenheit_entry = tk.Entry(fahrenheit_frame, width=15, font=("Arial", 11))
fahrenheit_entry.grid(row=0, column=1, padx=5)
convert_to_c_btn = tk.Button(fahrenheit_frame, text="Convert to °C", command=fahrenheit_to_celsius,
                              bg="#e74c3c", fg="white", font=("Arial", 10))
convert_to_c_btn.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
result_label.pack(pady=20)

# Clear button
clear_btn = tk.Button(root, text="Clear All", command=clear_fields, bg="#95a5a6", 
                      fg="white", font=("Arial", 10), width=15)
clear_btn.pack(pady=10)

root.mainloop()