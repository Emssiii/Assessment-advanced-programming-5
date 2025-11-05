import tkinter as tk
from tkinter import font

def analyze_text():
    text = input_entry.get()
    
    if not text.strip():
        result_label.config(text="Please enter some text!")
        return
    
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    special_count = 0
    letter_count = 0
    
    for char in text:
        if char.isalpha():
            letter_count += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char != ' ':
            special_count += 1
    
    result_text = f"""
Total number of letters: {letter_count}
Number of vowels: {vowel_count}
Number of consonants: {consonant_count}
Number of special characters: {special_count}
    """
    
    result_label.config(text=result_text)

# Create main window
root = tk.Tk()
root.title("Character Counter")
root.geometry("450x400")
root.config(bg="#f0f4f8")

# Create custom fonts
title_font = font.Font(family="Arial", size=18, weight="bold")
label_font = font.Font(family="Arial", size=11)
result_font = font.Font(family="Arial", size=12)

# Title
title_label = tk.Label(root, text="Character Counter", font=title_font, 
                       bg="#f0f4f8", fg="#1e3a8a")
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(pady=10, padx=20, fill="x")

input_label = tk.Label(input_frame, text="Enter a word or sentence:", 
                       font=label_font, bg="#f0f4f8", fg="#374151")
input_label.pack(anchor="w", pady=(0, 5))

input_entry = tk.Entry(input_frame, font=label_font, width=40, 
                      relief="solid", bd=2)
input_entry.pack(fill="x")

# Analyze button
analyze_btn = tk.Button(root, text="Analyze", command=analyze_text, 
                       font=label_font, bg="#4f46e5", fg="white", 
                       relief="flat", padx=20, pady=10, cursor="hand2",
                       activebackground="#4338ca")
analyze_btn.pack(pady=20)

# Results frame
result_frame = tk.Frame(root, bg="white", relief="solid", bd=1)
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_label = tk.Label(result_frame, text="Results will appear here...", 
                       font=result_font, bg="white", fg="#6b7280",
                       justify="left", pady=20)
result_label.pack()

# Bind Enter key to analyze
input_entry.bind('<Return>', lambda e: analyze_text())

root.mainloop()