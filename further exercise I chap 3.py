import tkinter as tk
from tkinter import messagebox

# --- Products and Prices ---
products = {
    "Coke": 2.5,
    "Pepsi": 2.0,
    "Water": 1.0,
    "Juice": 3.0,
    "Chips": 1.5,
    "Chocolate": 2.5
}

# --- Functions ---
def select_item(item):
    price = products[item]
    selected_item.set(item)
    item_price.set(f"Price: ${price:.2f}")

def buy_item():
    item = selected_item.get()
    if item == "":
        messagebox.showwarning("No Selection", "Please select an item first!")
        return
    
    price = products[item]
    try:
        money = float(money_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount of money.")
        return
    
    if money < price:
        messagebox.showinfo("Insufficient Funds", f"Not enough money! You need ${price - money:.2f} more.")
    else:
        change = money - price
        messagebox.showinfo("Enjoy!", f"You bought {item}!\nYour change is ${change:.2f}")
        money_entry.delete(0, tk.END)
        selected_item.set("")
        item_price.set("")

# --- GUI Setup ---
window = tk.Tk()
window.title("Vending Machine")
window.geometry("350x400")
window.config(bg="#f7f7f7")

selected_item = tk.StringVar()
item_price = tk.StringVar()

tk.Label(window, text="VENDING MACHINE", font=("Arial", 16, "bold"), bg="#f7f7f7").pack(pady=10)

# Product Buttons
frame = tk.Frame(window, bg="#f7f7f7")
frame.pack(pady=10)

for item, price in products.items():
    tk.Button(frame, text=f"{item} - ${price:.2f}", width=15, command=lambda i=item: select_item(i)).pack(pady=3)

# Display Selected Item
tk.Label(window, textvariable=selected_item, font=("Arial", 14), bg="#f7f7f7").pack(pady=5)
tk.Label(window, textvariable=item_price, font=("Arial", 12), bg="#f7f7f7").pack()

# Money Input
tk.Label(window, text="Insert Money:", bg="#f7f7f7").pack(pady=5)
money_entry = tk.Entry(window)
money_entry.pack()

# Buy Button
tk.Button(window, text="Buy", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), command=buy_item).pack(pady=10)

window.mainloop()
