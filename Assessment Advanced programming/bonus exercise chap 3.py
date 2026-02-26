import tkinter as tk
from tkinter import messagebox

# --- Data ---
burgers = {"Beef Burger": 8, "Chicken Burger": 7, "Veggie Burger": 6}
toppings = {"Cheese": 1, "Avocado": 1.5, "Bacon": 2}
condiments = {"Ketchup": 0.5, "Mayo": 0.5, "BBQ": 0.75}
sides = {"Fries": 3, "Drink": 2.5, "Onion Rings": 3.5}

# --- Functions ---
def calculate_total():
    total = burgers[burger_choice.get()]
    for cat in (toppings, condiments, sides):
        for name, price in cat.items():
            if vars_[name].get():
                total += price
    total_lbl.config(text=f"Total: ${total:.2f}")
    return total

def pay():
    try:
        payment = float(payment_entry.get())
        total = calculate_total()
        if payment < total:
            messagebox.showwarning("Not Enough", f"You need ${total - payment:.2f} more.")
        else:
            messagebox.showinfo("Order Complete", f"Thank you!\nChange: ${payment - total:.2f}")
            reset()
    except:
        messagebox.showerror("Error", "Enter valid payment amount.")

def reset():
    burger_choice.set("Beef Burger")
    for v in vars_.values(): v.set(False)
    total_lbl.config(text="Total: $0.00")
    payment_entry.delete(0, tk.END)

# --- GUI Setup ---
win = tk.Tk()
win.title("🍔 Burger Shack Ordering System")
win.geometry("500x650")
win.config(bg="#fff5e1")

title = tk.Label(win, text="🍔 BURGER SHACK 🍟", font=("Comic Sans MS", 22, "bold"), fg="#e63946", bg="#fff5e1")
title.pack(pady=10)

frame = tk.Frame(win, bg="#ffeedb", bd=5, relief="ridge")
frame.pack(pady=10, padx=20, fill="both", expand=True)

# --- Burger Selection ---
tk.Label(frame, text="Choose Your Burger:", font=("Arial", 14, "bold"), bg="#ffeedb", fg="#1d3557").pack(pady=5)
burger_choice = tk.StringVar(value="Beef Burger")
for b, p in burgers.items():
    tk.Radiobutton(frame, text=f"{b} - ${p}", variable=burger_choice, value=b, bg="#ffeedb", fg="#1d3557").pack(anchor="w", padx=30)

# --- Toppings / Condiments / Sides ---
vars_ = {}
for cat, data, color in [("Toppings", toppings, "#ffe3e3"), ("Condiments", condiments, "#e3f2fd"), ("Sides", sides, "#e8f5e9")]:
    tk.Label(frame, text=cat, font=("Arial", 13, "bold"), bg=color, fg="#333").pack(fill="x", pady=5)
    subf = tk.Frame(frame, bg=color)
    subf.pack(fill="x", padx=30)
    for name, price in data.items():
        vars_[name] = tk.BooleanVar()
        tk.Checkbutton(subf, text=f"{name} - ${price}", variable=vars_[name], bg=color, anchor="w").pack(anchor="w")

# --- Buttons & Payment ---
btn_frame = tk.Frame(win, bg="#fff5e1"); btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Calculate Total", command=calculate_total, bg="#2a9d8f", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset", command=reset, bg="#e76f51", fg="white", width=10).grid(row=0, column=1, padx=5)

total_lbl = tk.Label(win, text="Total: $0.00", font=("Arial", 14, "bold"), fg="#264653", bg="#fff5e1")
total_lbl.pack(pady=5)

tk.Label(win, text="Payment ($):", bg="#fff5e1", font=("Arial", 12)).pack()
payment_entry = tk.Entry(win, font=("Arial", 12))
payment_entry.pack(pady=5)
tk.Button(win, text="Pay Now", command=pay, bg="#457b9d", fg="white", font=("Arial", 12), width=15).pack(pady=10)

tk.Label(win, text="Thank you for dining with Burger Shack!", bg="#fff5e1", fg="#6d6875", font=("Arial", 10, "italic")).pack(pady=10)

win.mainloop()
