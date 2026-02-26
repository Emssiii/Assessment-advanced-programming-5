import tkinter as tk

# Create main window
root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("400x300")

# Create left frame
left_frame = tk.Frame(root, bd=5, relief=tk.RIDGE)
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Create right frame
right_frame = tk.Frame(root, bd=5, relief=tk.RIDGE)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Create label A in left frame (top)
label_a = tk.Label(left_frame, text="A", bg="#2b2d42", fg="white", font=("Arial", 16))
label_a.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Create label B in left frame (bottom)
label_b = tk.Label(left_frame, text="B", bg="#edf2f4", fg="black", font=("Arial", 16))
label_b.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

# Create label C in right frame (top)
label_c = tk.Label(right_frame, text="C", bg="#edf2f4", fg="black", font=("Arial", 16))
label_c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Create label D in right frame (bottom)
label_d = tk.Label(right_frame, text="D", bg="#2b2d42", fg="white", font=("Arial", 16))
label_d.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

# Start the GUI event loop
root.mainloop()