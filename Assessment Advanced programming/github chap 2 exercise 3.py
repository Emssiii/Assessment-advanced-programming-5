import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        messagebox.showwarning("Input Error", "Please fill in all fields")
    else:
        messagebox.showinfo("Login", f"Welcome, {username}!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create main frame with padding
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.grid(row=0, column=0, padx=50, pady=50)

# Title label
title_label = tk.Label(main_frame, text="Login", font=("Arial", 24, "bold"), 
                       bg="#f0f0f0", fg="#2b2d42")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# Username label
username_label = tk.Label(main_frame, text="Username:", font=("Arial", 12), 
                          bg="#f0f0f0", fg="#2b2d42")
username_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=10)

# Username entry
username_entry = tk.Entry(main_frame, font=("Arial", 12), width=20, 
                          relief=tk.SOLID, bd=1)
username_entry.grid(row=1, column=1, pady=10)

# Password label
password_label = tk.Label(main_frame, text="Password:", font=("Arial", 12), 
                          bg="#f0f0f0", fg="#2b2d42")
password_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=10)

# Password entry
password_entry = tk.Entry(main_frame, font=("Arial", 12), width=20, 
                          show="*", relief=tk.SOLID, bd=1)
password_entry.grid(row=2, column=1, pady=10)

# Button frame for horizontal button layout
button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))

# Login button
login_button = tk.Button(button_frame, text="Login", font=("Arial", 12, "bold"), 
                        bg="#2b2d42", fg="white", width=10, 
                        cursor="hand2", command=login)
login_button.grid(row=0, column=0, padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), 
                        bg="#8d99ae", fg="white", width=10, 
                        cursor="hand2", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)

# Center the main frame in the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
root.mainloop()