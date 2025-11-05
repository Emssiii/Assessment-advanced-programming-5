import tkinter as tk
from tkinter import ttk
import math

def calculate_circle():
    try:
        radius = float(circle_radius_entry.get())
        if radius <= 0:
            circle_result.config(text="Error: Radius must be positive!", fg="red")
            return
        area = math.pi * radius ** 2
        circle_result.config(text=f"Area: {area:.2f} square units", fg="green")
    except ValueError:
        circle_result.config(text="Error: Please enter a valid number!", fg="red")

def calculate_square():
    try:
        side = float(square_side_entry.get())
        if side <= 0:
            square_result.config(text="Error: Side must be positive!", fg="red")
            return
        area = side ** 2
        square_result.config(text=f"Area: {area:.2f} square units", fg="green")
    except ValueError:
        square_result.config(text="Error: Please enter a valid number!", fg="red")

def calculate_rectangle():
    try:
        length = float(rect_length_entry.get())
        width = float(rect_width_entry.get())
        if length <= 0 or width <= 0:
            rect_result.config(text="Error: Dimensions must be positive!", fg="red")
            return
        area = length * width
        rect_result.config(text=f"Area: {area:.2f} square units", fg="green")
    except ValueError:
        rect_result.config(text="Error: Please enter valid numbers!", fg="red")

# Create main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("500x400")
root.config(bg="#f0f4f8")

# Title
title_label = tk.Label(root, text="📐 Area Calculator", 
                       font=("Arial", 20, "bold"), 
                       fg="#1e3a8a", bg="#f0f4f8")
title_label.pack(pady=15)

# Create notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(padx=20, pady=10, fill="both", expand=True)

# ===== CIRCLE TAB =====
circle_frame = tk.Frame(notebook, bg="#e0f2fe")
notebook.add(circle_frame, text="Circle")

tk.Label(circle_frame, text="Calculate Circle Area", 
         font=("Arial", 14, "bold"), bg="#e0f2fe", fg="#0c4a6e").pack(pady=20)

tk.Label(circle_frame, text="Enter Radius:", 
         font=("Arial", 11), bg="#e0f2fe").pack(pady=5)

circle_radius_entry = tk.Entry(circle_frame, font=("Arial", 12), width=20)
circle_radius_entry.pack(pady=5)

circle_btn = tk.Button(circle_frame, text="Calculate Area", 
                       command=calculate_circle,
                       font=("Arial", 11, "bold"), 
                       bg="#0284c7", fg="white", 
                       padx=20, pady=8, cursor="hand2")
circle_btn.pack(pady=15)

circle_result = tk.Label(circle_frame, text="", 
                        font=("Arial", 12, "bold"), bg="#e0f2fe")
circle_result.pack(pady=10)

tk.Label(circle_frame, text="Formula: A = πr²", 
         font=("Arial", 9, "italic"), bg="#e0f2fe", fg="#475569").pack(pady=5)

circle_radius_entry.bind('<Return>', lambda e: calculate_circle())

# ===== SQUARE TAB =====
square_frame = tk.Frame(notebook, bg="#fef3c7")
notebook.add(square_frame, text="Square")

tk.Label(square_frame, text="Calculate Square Area", 
         font=("Arial", 14, "bold"), bg="#fef3c7", fg="#78350f").pack(pady=20)

tk.Label(square_frame, text="Enter Side Length:", 
         font=("Arial", 11), bg="#fef3c7").pack(pady=5)

square_side_entry = tk.Entry(square_frame, font=("Arial", 12), width=20)
square_side_entry.pack(pady=5)

square_btn = tk.Button(square_frame, text="Calculate Area", 
                       command=calculate_square,
                       font=("Arial", 11, "bold"), 
                       bg="#f59e0b", fg="white", 
                       padx=20, pady=8, cursor="hand2")
square_btn.pack(pady=15)

square_result = tk.Label(square_frame, text="", 
                        font=("Arial", 12, "bold"), bg="#fef3c7")
square_result.pack(pady=10)

tk.Label(square_frame, text="Formula: A = s²", 
         font=("Arial", 9, "italic"), bg="#fef3c7", fg="#475569").pack(pady=5)

square_side_entry.bind('<Return>', lambda e: calculate_square())

# ===== RECTANGLE TAB =====
rectangle_frame = tk.Frame(notebook, bg="#dcfce7")
notebook.add(rectangle_frame, text="Rectangle")

tk.Label(rectangle_frame, text="Calculate Rectangle Area", 
         font=("Arial", 14, "bold"), bg="#dcfce7", fg="#14532d").pack(pady=20)

tk.Label(rectangle_frame, text="Enter Length:", 
         font=("Arial", 11), bg="#dcfce7").pack(pady=5)

rect_length_entry = tk.Entry(rectangle_frame, font=("Arial", 12), width=20)
rect_length_entry.pack(pady=5)

tk.Label(rectangle_frame, text="Enter Width:", 
         font=("Arial", 11), bg="#dcfce7").pack(pady=5)

rect_width_entry = tk.Entry(rectangle_frame, font=("Arial", 12), width=20)
rect_width_entry.pack(pady=5)

rect_btn = tk.Button(rectangle_frame, text="Calculate Area", 
                     command=calculate_rectangle,
                     font=("Arial", 11, "bold"), 
                     bg="#16a34a", fg="white", 
                     padx=20, pady=8, cursor="hand2")
rect_btn.pack(pady=15)

rect_result = tk.Label(rectangle_frame, text="", 
                      font=("Arial", 12, "bold"), bg="#dcfce7")
rect_result.pack(pady=10)

tk.Label(rectangle_frame, text="Formula: A = l × w", 
         font=("Arial", 9, "italic"), bg="#dcfce7", fg="#475569").pack(pady=5)

rect_width_entry.bind('<Return>', lambda e: calculate_rectangle())

root.mainloop()