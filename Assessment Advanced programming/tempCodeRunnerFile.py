import tkinter as tk

# Create main window
root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("460x280")

# Create label A (red, at top with some margin below title)
label_a = tk.Label(root, text="A", bg="red", fg="black", height=1)
label_a.place(x=0, y=115, relwidth=1)

# Create label C (blue, at bottom left)
label_c = tk.Label(root, text="C", bg="blue", fg="white")
label_c.place(x=118, y=225, width=115, height=30)

# Create label B (yellow, at bottom middle)
label_b = tk.Label(root, text="B", bg="yellow", fg="black")
label_b.place(x=178, y=255, width=115, height=25)

# Create label D (white background, at bottom right)
label_d = tk.Label(root, text="D", bg="white", fg="black")
label_d.place(x=360, y=225, width=115, height=30)

root.mainloop()