import tkinter as tk
from tkinter import font

window = tk.Tk()
window.title("Welcome Window")

window.geometry("400x250")

window.resizable(False, False)

window.config(bg="lightblue")

welcome_font = ("Arial", 18, "bold")
welcome_label = tk.Label(window, text="Welcome to Tkinter GUI!", font=welcome_font, bg="lightblue", fg="darkblue")
welcome_label.pack(pady=80)

window.mainloop()
