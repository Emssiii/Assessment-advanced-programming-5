import tkinter as tk
from tkinter import messagebox
import random

words = ["python", "burger", "window", "laptop", "game"]
score = 0

def new_word():
    global w, shuffled
    w = random.choice(words)
    shuffled = ''.join(random.sample(w, len(w)))
    lbl_word.config(text=shuffled)
    entry.delete(0, tk.END)

def check():
    global score
    guess = entry.get().lower()
    if guess == w:
        score += 1
        messagebox.showinfo("Correct!", f"Good job! Score: {score}")
    else:
        messagebox.showinfo("Wrong!", f"Answer: {w}")
    new_word()

win = tk.Tk(); win.title("Guess the Word"); win.geometry("300x250")
tk.Label(win, text="Guess the Word!", font=("Arial", 16, "bold")).pack(pady=10)
lbl_word = tk.Label(win, text="", font=("Arial", 20)); lbl_word.pack(pady=10)
entry = tk.Entry(win); entry.pack()
tk.Button(win, text="Check", bg="#4CAF50", fg="white", command=check).pack(pady=5)
tk.Button(win, text="New Word", bg="#2196F3", fg="white", command=new_word).pack(pady=5)
new_word()
win.mainloop()
