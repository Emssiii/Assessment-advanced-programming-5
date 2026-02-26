import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    gender = gender_var.get()
    course = course_var.get()
    english_rating = english_scale.get()
    
    languages = []
    if english_var.get():
        languages.append("English")
    if tagalog_var.get():
        languages.append("Tagalog")
    if hindi_var.get():
        languages.append("Hindi/Urdu")
    
    if not name or not mobile or not email or not address:
        messagebox.showwarning("Validation Error", "Please fill in all fields")
        return
    
    msg = f"Registration Successful!\n\nName: {name}\nMobile: {mobile}\nEmail: {email}\n"
    msg += f"Gender: {gender}\nCourse: {course}\nLanguages: {', '.join(languages)}\n"
    msg += f"English Skills: {english_rating}/100"
    messagebox.showinfo("Success", msg)

def clear_form():
    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    gender_var.set("")
    course_var.set("")
    english_var.set(0)
    tagalog_var.set(0)
    hindi_var.set(0)
    english_scale.set(0)

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("450x750")
root.configure(bg="white")

# Header
header_frame = tk.Frame(root, bg="#2b3e50", height=60)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

tk.Label(header_frame, text="BATH SPA UNIVERSITY  |  RAK CAMPUS", font=("Arial", 14, "bold"), 
         bg="#2b3e50", fg="white").pack(pady=15)

# Content
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)

# Title
tk.Label(content_frame, text="Student Management System", font=("Arial", 16, "bold"), 
         bg="white", fg="#2b3e50").pack()
tk.Label(content_frame, text="New Student Registration", font=("Arial", 12), 
         bg="white", fg="#5a6c7d").pack(pady=(0, 15))

# Form
form_frame = tk.Frame(content_frame, bg="white")
form_frame.pack()

# Student Name
tk.Label(form_frame, text="Student Name", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, font=("Arial", 10), bg="#c8d0d8", relief=tk.FLAT, width=40)
name_entry.grid(row=0, column=1, pady=3, ipady=3)

# Mobile Number
tk.Label(form_frame, text="Mobile Number", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=1, column=0, sticky="w")
mobile_entry = tk.Entry(form_frame, font=("Arial", 10), bg="#c8d0d8", relief=tk.FLAT, width=40)
mobile_entry.grid(row=1, column=1, pady=3, ipady=3)

# Email Id
tk.Label(form_frame, text="Email Id", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(form_frame, font=("Arial", 10), bg="#c8d0d8", relief=tk.FLAT, width=40)
email_entry.grid(row=2, column=1, pady=3, ipady=3)

# Home Address
tk.Label(form_frame, text="Home Address", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(form_frame, font=("Arial", 10), bg="#c8d0d8", relief=tk.FLAT, width=40)
address_entry.grid(row=3, column=1, pady=3, ipady=3)

# Gender
tk.Label(form_frame, text="Gender", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=4, column=0, sticky="w")
gender_var = tk.StringVar()
gender_combo = ttk.Combobox(form_frame, textvariable=gender_var, font=("Arial", 10), 
                            width=38, state="readonly")
gender_combo['values'] = ('Male', 'Female', 'Other')
gender_combo.grid(row=4, column=1, pady=3, ipady=2)

# Course Enrolled
tk.Label(form_frame, text="Course Enrolled", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=5, column=0, sticky="nw", pady=(5, 0))

course_var = tk.StringVar()
radio_frame = tk.Frame(form_frame, bg="white")
radio_frame.grid(row=5, column=1, sticky="w", pady=3)

tk.Radiobutton(radio_frame, text="BSc CC", variable=course_var, value="BSc CC", 
               font=("Arial", 9), bg="white").pack(anchor="w", pady=1)
tk.Radiobutton(radio_frame, text="BSc CY", variable=course_var, value="BSc CY", 
               font=("Arial", 9), bg="white").pack(anchor="w", pady=1)
tk.Radiobutton(radio_frame, text="BSc PSY", variable=course_var, value="BSc PSY", 
               font=("Arial", 9), bg="white").pack(anchor="w", pady=1)
tk.Radiobutton(radio_frame, text="BA & BM", variable=course_var, value="BA & BM", 
               font=("Arial", 9), bg="white").pack(anchor="w", pady=1)

# Languages known
tk.Label(form_frame, text="Languages known", font=("Arial", 9), bg="white", 
         fg="#5a6c7d", anchor="w").grid(row=6, column=0, sticky="nw", pady=(5, 0))

english_var = tk.IntVar()
tagalog_var = tk.IntVar()
hindi_var = tk.IntVar()

checkbox_frame = tk.Frame(form_frame, bg="white")
checkbox_frame.grid(row=6, column=1, sticky="w", pady=3)

lang_row = tk.Frame(checkbox_frame, bg="white")
lang_row.pack(anchor="w")
tk.Checkbutton(lang_row, text="English", variable=english_var, font=("Arial", 9), 
               bg="white").pack(side=tk.LEFT)
tk.Checkbutton(lang_row, text="Tagalog", variable=tagalog_var, font=("Arial", 9), 
               bg="white").pack(side=tk.LEFT)

tk.Checkbutton(checkbox_frame, text="Hindi/Urdu", variable=hindi_var, font=("Arial", 9), 
               bg="white").pack(anchor="w")

# Rate English skills
tk.Label(form_frame, text="Rate your English communication skills", font=("Arial", 9), 
         bg="white", fg="#5a6c7d").grid(row=7, column=0, columnspan=2, sticky="w", pady=(10, 5))

english_scale = tk.Scale(form_frame, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", 
                         length=300, troughcolor="#c8d0d8", sliderlength=15, 
                         highlightthickness=0, showvalue=0)
english_scale.grid(row=8, column=0, columnspan=2, pady=(0, 15))

# Buttons
button_frame = tk.Frame(content_frame, bg="white")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit", font=("Arial", 11, "bold"), bg="#2b3e50", 
          fg="white", width=12, height=1, cursor="hand2", relief=tk.FLAT, 
          command=submit_form).grid(row=0, column=0, padx=15)

tk.Button(button_frame, text="Clear", font=("Arial", 11, "bold"), bg="#2b3e50", 
          fg="white", width=12, height=1, cursor="hand2", relief=tk.FLAT, 
          command=clear_form).grid(row=0, column=1, padx=15)

root.mainloop()