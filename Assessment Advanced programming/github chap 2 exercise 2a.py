import tkinter as tk

root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("190x80")
root.config(bg="#e0e0e0")  

label_a = tk.Label(root, text="A", bg="red", bd=6, relief="ridge").pack(fill="x", side="top", anchor="center", expand=1)

bottom_frame1 = tk.Frame(root, bg="#e0e0e0")
bottom_frame1.pack(side="bottom", anchor="n", fill="x")
bottom_frame2 = tk.Frame(root, bg="#e0e0e0")
bottom_frame2.pack(side="bottom", anchor="s", fill="x")
label_d = tk.Label(bottom_frame2, text="D", bg="white", width=13).pack(anchor="center", side="right")
label_c = tk.Label(bottom_frame2, text="C", bg="blue", width=13).pack(anchor="center")
label_b = tk.Label(bottom_frame1, text="B", bg="yellow", bd=5, relief = "raised", width=13).pack(side="bottom", anchor="center")

root.mainloop()