import tkinter as tk
from tkinter import ttk, messagebox

def draw_shape():
    shape = shape_var.get()
    
    if not shape:
        messagebox.showwarning("Warning", "Please select a shape!")
        return
    
    # Clear canvas
    canvas.delete("all")
    
    # Get coordinates if user wants custom input
    if use_custom_coords.get():
        try:
            x1 = float(x1_entry.get())
            y1 = float(y1_entry.get())
            x2 = float(x2_entry.get())
            y2 = float(y2_entry.get())
            
            # Validate coordinates
            if not (0 <= x1 <= 400 and 0 <= y1 <= 400 and 
                   0 <= x2 <= 400 and 0 <= y2 <= 400):
                messagebox.showerror("Error", "Coordinates must be between 0 and 400!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for coordinates!")
            return
    else:
        # Default coordinates (centered)
        x1, y1 = 100, 100
        x2, y2 = 300, 300
    
    # Get selected color
    color = color_var.get()
    
    # Draw the selected shape
    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black", width=2)
    elif shape == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
    elif shape == "Square":
        # Make it a square by using equal width and height
        side = min(x2 - x1, y2 - y1)
        canvas.create_rectangle(x1, y1, x1 + side, y1 + side, 
                               fill=color, outline="black", width=2)
    elif shape == "Triangle":
        # Calculate triangle points
        mid_x = (x1 + x2) / 2
        canvas.create_polygon(mid_x, y1, x1, y2, x2, y2, 
                             fill=color, outline="black", width=2)

def clear_canvas():
    canvas.delete("all")
    shape_var.set("")
    x1_entry.delete(0, tk.END)
    y1_entry.delete(0, tk.END)
    x2_entry.delete(0, tk.END)
    y2_entry.delete(0, tk.END)

def toggle_coordinate_input():
    if use_custom_coords.get():
        coord_frame.pack(pady=10, padx=20, fill="x")
    else:
        coord_frame.pack_forget()

# Create main window
root = tk.Tk()
root.title("Shape Drawing App")
root.geometry("700x650")
root.config(bg="#f0f4f8")

# Title
title_label = tk.Label(root, text="🎨 Shape Drawing App", 
                       font=("Arial", 20, "bold"), 
                       fg="#1e3a8a", bg="#f0f4f8")
title_label.pack(pady=15)

# Control panel frame
control_frame = tk.Frame(root, bg="#e0e7ff", relief="ridge", bd=2)
control_frame.pack(padx=20, pady=10, fill="x")

# Shape selection
tk.Label(control_frame, text="Select Shape:", 
         font=("Arial", 11, "bold"), bg="#e0e7ff").pack(pady=10)

shape_var = tk.StringVar()

shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_combo = ttk.Combobox(control_frame, textvariable=shape_var, 
                          values=shapes, font=("Arial", 11), 
                          state="readonly", width=18)
shape_combo.pack(pady=5)

# Color selection
tk.Label(control_frame, text="Select Color:", 
         font=("Arial", 11, "bold"), bg="#e0e7ff").pack(pady=10)

color_var = tk.StringVar(value="lightblue")

colors = ["lightblue", "lightgreen", "lightcoral", "lightyellow", 
          "lightpink", "lavender", "peachpuff", "lightcyan"]
color_combo = ttk.Combobox(control_frame, textvariable=color_var, 
                          values=colors, font=("Arial", 11), 
                          state="readonly", width=18)
color_combo.pack(pady=5)

# Custom coordinates checkbox
use_custom_coords = tk.BooleanVar()
coord_checkbox = tk.Checkbutton(control_frame, 
                               text="Use Custom Coordinates (0-400)", 
                               variable=use_custom_coords,
                               command=toggle_coordinate_input,
                               font=("Arial", 10), bg="#e0e7ff",
                               activebackground="#e0e7ff")
coord_checkbox.pack(pady=10)

# Coordinate input frame (hidden by default)
coord_frame = tk.Frame(control_frame, bg="#e0e7ff")

tk.Label(coord_frame, text="x1:", font=("Arial", 9), bg="#e0e7ff").grid(row=0, column=0, padx=5)
x1_entry = tk.Entry(coord_frame, font=("Arial", 10), width=8)
x1_entry.grid(row=0, column=1, padx=5)

tk.Label(coord_frame, text="y1:", font=("Arial", 9), bg="#e0e7ff").grid(row=0, column=2, padx=5)
y1_entry = tk.Entry(coord_frame, font=("Arial", 10), width=8)
y1_entry.grid(row=0, column=3, padx=5)

tk.Label(coord_frame, text="x2:", font=("Arial", 9), bg="#e0e7ff").grid(row=1, column=0, padx=5, pady=5)
x2_entry = tk.Entry(coord_frame, font=("Arial", 10), width=8)
x2_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(coord_frame, text="y2:", font=("Arial", 9), bg="#e0e7ff").grid(row=1, column=2, padx=5, pady=5)
y2_entry = tk.Entry(coord_frame, font=("Arial", 10), width=8)
y2_entry.grid(row=1, column=3, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(control_frame, bg="#e0e7ff")
button_frame.pack(pady=10)

draw_btn = tk.Button(button_frame, text="Draw Shape", 
                    command=draw_shape,
                    font=("Arial", 11, "bold"), 
                    bg="#4f46e5", fg="white", 
                    padx=20, pady=8, cursor="hand2")
draw_btn.pack(side="left", padx=5)

clear_btn = tk.Button(button_frame, text="Clear Canvas", 
                     command=clear_canvas,
                     font=("Arial", 11, "bold"), 
                     bg="#dc2626", fg="white", 
                     padx=20, pady=8, cursor="hand2")
clear_btn.pack(side="left", padx=5)

# Canvas frame
canvas_frame = tk.Frame(root, bg="white", relief="sunken", bd=3)
canvas_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Canvas
canvas = tk.Canvas(canvas_frame, width=400, height=400, bg="white")
canvas.pack(padx=5, pady=5)

# Instructions
instructions = tk.Label(root, 
                       text="Default coordinates: (100,100) to (300,300)", 
                       font=("Arial", 9, "italic"), 
                       bg="#f0f4f8", fg="#475569")
instructions.pack(pady=5)

root.mainloop()