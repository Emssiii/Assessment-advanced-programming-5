import tkinter as tk
from tkinter import messagebox

# Create main window first
root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("450x500")
root.configure(bg="#f5f5f5")

# Define functions after root is created
def perform_operation(operation):
    print(f"Button clicked: {operation}")  # Debug print
    try:
        val1 = entry1.get()
        val2 = entry2.get()
        
        print(f"Values: {val1}, {val2}")  # Debug print
        
        if val1 == "" or val2 == "":
            messagebox.showerror("Error", "Please enter both numbers!")
            return
        
        num1 = float(val1)
        num2 = float(val2)
        
        result = 0
        op_symbol = ""
        
        if operation == "add":
            result = num1 + num2
            op_symbol = "+"
        elif operation == "subtract":
            result = num1 - num2
            op_symbol = "-"
        elif operation == "multiply":
            result = num1 * num2
            op_symbol = "×"
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
            op_symbol = "÷"
        elif operation == "modulo":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot perform modulo with zero!")
                result_label.config(text="Error: Modulo by zero")
                return
            result = num1 % num2
            op_symbol = "%"
        
        # Format result
        if isinstance(result, float) and result.is_integer():
            result_text = f"{int(num1)} {op_symbol} {int(num2)} = {int(result)}"
        else:
            result_text = f"{num1} {op_symbol} {num2} = {round(result, 4)}"
        
        print(f"Result: {result_text}")  # Debug print
        result_label.config(text=result_text)
        result_label.update()
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
        messagebox.showerror("Error", "Please enter valid numbers!")
        result_label.config(text="Error: Invalid input")
    except Exception as e:
        print(f"Exception: {e}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        result_label.config(text="Error occurred")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="")

# Title
title_label = tk.Label(root, text="Basic Arithmetic Calculator", 
                       font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#2c3e50")
title_label.pack(pady=20)

# Input Frame
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=20)

# First Number
tk.Label(input_frame, text="First Number:", font=("Arial", 12), 
         bg="#f5f5f5", fg="#34495e").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(input_frame, font=("Arial", 14), width=20, 
                  relief=tk.SOLID, bd=1, bg="white")
entry1.grid(row=0, column=1, padx=10, pady=10)

# Second Number
tk.Label(input_frame, text="Second Number:", font=("Arial", 12), 
         bg="#f5f5f5", fg="#34495e").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(input_frame, font=("Arial", 14), width=20, 
                  relief=tk.SOLID, bd=1, bg="white")
entry2.grid(row=1, column=1, padx=10, pady=10)

# Operation Buttons Frame
operation_frame = tk.Frame(root, bg="#f5f5f5")
operation_frame.pack(pady=20)

tk.Label(operation_frame, text="Select Operation:", font=("Arial", 12, "bold"), 
         bg="#f5f5f5", fg="#34495e").pack(pady=(0, 15))

# Button Frame
button_frame = tk.Frame(operation_frame, bg="#f5f5f5")
button_frame.pack()

# Row 1 buttons
row1 = tk.Frame(button_frame, bg="#f5f5f5")
row1.pack(pady=5)

add_btn = tk.Button(row1, text="Addition (+)", font=("Arial", 12, "bold"), 
          bg="#27ae60", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=lambda: perform_operation("add"))
add_btn.pack(side=tk.LEFT, padx=5)

sub_btn = tk.Button(row1, text="Subtraction (-)", font=("Arial", 12, "bold"), 
          bg="#e74c3c", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=lambda: perform_operation("subtract"))
sub_btn.pack(side=tk.LEFT, padx=5)

# Row 2 buttons
row2 = tk.Frame(button_frame, bg="#f5f5f5")
row2.pack(pady=5)

mul_btn = tk.Button(row2, text="Multiplication (×)", font=("Arial", 12, "bold"), 
          bg="#3498db", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=lambda: perform_operation("multiply"))
mul_btn.pack(side=tk.LEFT, padx=5)

div_btn = tk.Button(row2, text="Division (÷)", font=("Arial", 12, "bold"), 
          bg="#f39c12", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=lambda: perform_operation("divide"))
div_btn.pack(side=tk.LEFT, padx=5)

# Row 3 buttons
row3 = tk.Frame(button_frame, bg="#f5f5f5")
row3.pack(pady=5)

mod_btn = tk.Button(row3, text="Modulo (%)", font=("Arial", 12, "bold"), 
          bg="#9b59b6", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=lambda: perform_operation("modulo"))
mod_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(row3, text="Clear", font=("Arial", 12, "bold"), 
          bg="#95a5a6", fg="white", width=15, height=2, 
          cursor="hand2", relief=tk.RAISED, bd=3,
          command=clear_all)
clear_btn.pack(side=tk.LEFT, padx=5)

# Result Frame
result_frame = tk.Frame(root, bg="#ecf0f1", relief=tk.SOLID, bd=2)
result_frame.pack(pady=20, padx=30, fill=tk.X)

tk.Label(result_frame, text="Result:", font=("Arial", 12, "bold"), 
         bg="#ecf0f1", fg="#2c3e50").pack(pady=(10, 5))

result_label = tk.Label(result_frame, text="", 
                        font=("Arial", 16, "bold"), bg="#ecf0f1", 
                        fg="#16a085", height=2)
result_label.pack(pady=(0, 10))

# Start the GUI event loop
root.mainloop()