import tkinter as tk
from tkinter import font

def convert_to_uppercase():
    text = input_entry.get()
    uppercase_text = text.upper()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, uppercase_text)

# Create main window
root = tk.Tk()
root.title("Uppercase Converter")
root.geometry("500x350")
root.config(bg="#f0f4f8")

# Create custom fonts
title_font = font.Font(family="Arial", size=18, weight="bold")
label_font = font.Font(family="Arial", size=11)

# Title
title_label = tk.Label(root, text="Uppercase Converter", font=title_font, 
                       bg="#f0f4f8", fg="#1e3a8a")
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(pady=10, padx=30, fill="x")

input_label = tk.Label(input_frame, text="Enter text:", 
                       font=label_font, bg="#f0f4f8", fg="#374151")
input_label.pack(anchor="w", pady=(0, 5))

input_entry = tk.Entry(input_frame, font=label_font, width=50, 
                      relief="solid", bd=2)
input_entry.pack(fill="x")

# Convert button
convert_btn = tk.Button(root, text="Convert to UPPERCASE", 
                       command=convert_to_uppercase, 
                       font=label_font, bg="#4f46e5", fg="white", 
                       relief="flat", padx=20, pady=10, cursor="hand2",
                       activebackground="#4338ca")
convert_btn.pack(pady=20)

# Result frame
result_frame = tk.Frame(root, bg="#f0f4f8")
result_frame.pack(pady=10, padx=30, fill="x")

result_label = tk.Label(result_frame, text="Result:", 
                       font=label_font, bg="#f0f4f8", fg="#374151")
result_label.pack(anchor="w", pady=(0, 5))

result_entry = tk.Entry(result_frame, font=label_font, width=50, 
                       relief="solid", bd=2, state="normal")
result_entry.pack(fill="x")

# Bind Enter key to convert
input_entry.bind('<Return>', lambda e: convert_to_uppercase())

root.mainloop()