"""
=======================================================
EXERCISE B: AGE CALCULATOR
=======================================================
A program to take input of the user's date of birth 
and output the age.
Expected input: 8/5/2018
Expected output: Your age is 5 years
Hint: Uses the date from datetime package to get 
today's date
=======================================================
"""

import tkinter as tk
from datetime import date

def calculate_age():
    try:
        # Get the input date
        dob_input = dob_entry.get()
        
        # Parse the date (expecting format: M/D/YYYY or MM/DD/YYYY)
        parts = dob_input.split('/')
        if len(parts) != 3:
            result_label.config(text="Invalid format! Use M/D/YYYY", fg="red")
            return
        
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        
        # Create date object for birth date
        birth_date = date(year, month, day)
        
        # Get today's date
        today = date.today()
        
        # Calculate age
        age = today.year - birth_date.year
        
        # Adjust if birthday hasn't occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        # Display result
        if age < 0:
            result_label.config(text="Birth date cannot be in the future!", fg="red")
        elif age == 0:
            result_label.config(text="Your age is less than 1 year", fg="green")
        elif age == 1:
            result_label.config(text="Your age is 1 year", fg="green")
        else:
            result_label.config(text=f"Your age is {age} years", fg="green")
            
    except ValueError:
        result_label.config(text="Invalid date! Please check your input.", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def clear_fields():
    dob_entry.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Exercise B: Age Calculator")
root.geometry("400x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), fg="#2c3e50")
title_label.pack(pady=15)

# Instructions
instruction_label = tk.Label(root, text="Enter your date of birth (M/D/YYYY):", 
                             font=("Arial", 11))
instruction_label.pack(pady=5)

# Date of birth entry
dob_entry = tk.Entry(root, width=20, font=("Arial", 12), justify='center')
dob_entry.pack(pady=10)
dob_entry.insert(0, "8/5/2018")  # Example placeholder

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Calculate button
calculate_btn = tk.Button(button_frame, text="Calculate Age", command=calculate_age,
                          bg="#27ae60", fg="white", font=("Arial", 11), width=12)
calculate_btn.grid(row=0, column=0, padx=5)

# Clear button
clear_btn = tk.Button(button_frame, text="Clear", command=clear_fields,
                      bg="#95a5a6", fg="white", font=("Arial", 11), width=12)
clear_btn.grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="green")
result_label.pack(pady=15)

root.mainloop()