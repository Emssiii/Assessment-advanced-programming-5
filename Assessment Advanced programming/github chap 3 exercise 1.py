import tkinter as tk
from tkinter import ttk

def update_greeting():
    name = name_entry.get()
    color = color_combo.get()
    
    if name:
        greeting_text = f"Hello, {name}! Welcome!"
        greeting_label.config(text=greeting_text, fg=color)
    else:
        greeting_label.config(text="Please enter your name!", fg="red")

# Create main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("500x400")

# InputFrame
input_frame = tk.Frame(root, bg="#e3f2fd", relief="ridge", bd=3)
input_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# Title label in blue
title_label = tk.Label(input_frame, text="Greeting App", 
                       font=("Arial", 18, "bold"), 
                       fg="blue", bg="#e3f2fd")
title_label.pack(pady=15)

# Name entry
name_label = tk.Label(input_frame, text="Enter your name:", 
                      font=("Arial", 11), bg="#e3f2fd")
name_label.pack(pady=5)

name_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
name_entry.pack(pady=5)

# Color dropdown
color_label = tk.Label(input_frame, text="Select a color:", 
                       font=("Arial", 11), bg="#e3f2fd")
color_label.pack(pady=5)

color_combo = ttk.Combobox(input_frame, font=("Arial", 11), width=28, 
                           state="readonly")
color_combo['values'] = ("Red", "Blue", "Green", "Purple", "Orange", 
                          "Brown", "Pink", "Cyan")
color_combo.current(0)
color_combo.pack(pady=5)

# Update button
update_btn = tk.Button(input_frame, text="Update Greeting", 
                       command=update_greeting,
                       font=("Arial", 11, "bold"), 
                       bg="#4CAF50", fg="white", 
                       padx=20, pady=8, cursor="hand2")
update_btn.pack(pady=15)

# DisplayFrame
display_frame = tk.Frame(root, bg="#fff9c4", relief="ridge", bd=3)
display_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

# Greeting label (initially empty)
greeting_label = tk.Label(display_frame, text="", 
                         font=("Arial", 14, "bold"), 
                         bg="#fff9c4", wraplength=450)
greeting_label.pack(expand=True)

# Bind Enter key
name_entry.bind('<Return>', lambda e: update_greeting())

root.mainloop()