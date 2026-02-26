import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def place_order():
    coffee_type = coffee_var.get()
    
    if not coffee_type:
        messagebox.showwarning("Warning", "Please select a coffee type!")
        return
    
    # Get selected options
    options = []
    if sugar_var.get():
        options.append("Sugar")
    if milk_var.get():
        options.append("Milk")
    if cream_var.get():
        options.append("Cream")
    if vanilla_var.get():
        options.append("Vanilla")
    
    # Build order message
    order_msg = f"☕ Your Order ☕\n\n"
    order_msg += f"Coffee Type: {coffee_type}\n"
    
    if options:
        order_msg += f"Add-ons: {', '.join(options)}\n"
    else:
        order_msg += "Add-ons: None\n"
    
    order_msg += f"\nPrice: ${calculate_price(coffee_type, len(options)):.2f}"
    order_msg += "\n\nThank you for your order!"
    
    messagebox.showinfo("Order Confirmation", order_msg)

def calculate_price(coffee_type, num_options):
    base_prices = {
        "Espresso": 2.50,
        "Cappuccino": 3.50,
        "Latte": 3.75,
        "Americano": 2.75,
        "Mocha": 4.00
    }
    base = base_prices.get(coffee_type, 3.00)
    return base + (num_options * 0.50)

def handle_payment():
    coffee_type = coffee_var.get()
    
    if not coffee_type:
        messagebox.showwarning("Warning", "Please select a coffee type first!")
        return
    
    options_count = sum([sugar_var.get(), milk_var.get(), 
                        cream_var.get(), vanilla_var.get()])
    total = calculate_price(coffee_type, options_count)
    
    # Create payment window
    payment_window = tk.Toplevel(root)
    payment_window.title("Payment")
    payment_window.geometry("350x250")
    payment_window.config(bg="#f0f4f8")
    
    tk.Label(payment_window, text=f"Total Amount: ${total:.2f}", 
             font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=15)
    
    tk.Label(payment_window, text="Enter amount paid:", 
             font=("Arial", 11), bg="#f0f4f8").pack(pady=5)
    
    amount_entry = tk.Entry(payment_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)
    amount_entry.focus()
    
    def process_payment():
        try:
            paid = float(amount_entry.get())
            if paid < total:
                messagebox.showerror("Error", 
                    f"Insufficient payment! You need ${total - paid:.2f} more.")
            else:
                change = paid - total
                messagebox.showinfo("Payment Success", 
                    f"Payment received!\nChange: ${change:.2f}\n\nEnjoy your coffee! ☕")
                payment_window.destroy()
                # Reset form
                coffee_var.set("")
                sugar_var.set(False)
                milk_var.set(False)
                cream_var.set(False)
                vanilla_var.set(False)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")
    
    pay_btn = tk.Button(payment_window, text="Pay", command=process_payment,
                       font=("Arial", 11, "bold"), bg="#4CAF50", fg="white",
                       padx=30, pady=8)
    pay_btn.pack(pady=15)
    
    amount_entry.bind('<Return>', lambda e: process_payment())

# Create main window
root = tk.Tk()
root.title("☕ Coffee Vending Machine")
root.geometry("450x550")
root.config(bg="#6f4e37")

# Title with coffee emoji
title_label = tk.Label(root, text="☕ Coffee Vending Machine ☕", 
                       font=("Arial", 20, "bold"), 
                       fg="white", bg="#6f4e37")
title_label.pack(pady=20)

# Main frame
main_frame = tk.Frame(root, bg="#f5deb3", relief="ridge", bd=3)
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Coffee selection
tk.Label(main_frame, text="Select Coffee Type:", 
         font=("Arial", 12, "bold"), bg="#f5deb3").pack(pady=10)

coffee_var = tk.StringVar()

coffee_types = [
    ("☕ Espresso - $2.50", "Espresso"),
    ("☕ Cappuccino - $3.50", "Cappuccino"),
    ("☕ Latte - $3.75", "Latte"),
    ("☕ Americano - $2.75", "Americano"),
    ("☕ Mocha - $4.00", "Mocha")
]

for text, value in coffee_types:
    tk.Radiobutton(main_frame, text=text, variable=coffee_var, 
                   value=value, font=("Arial", 10),
                   bg="#f5deb3", activebackground="#f5deb3").pack(anchor="w", padx=40)

# Options section
tk.Label(main_frame, text="Add-ons (+ $0.50 each):", 
         font=("Arial", 12, "bold"), bg="#f5deb3").pack(pady=15)

sugar_var = tk.BooleanVar()
milk_var = tk.BooleanVar()
cream_var = tk.BooleanVar()
vanilla_var = tk.BooleanVar()

tk.Checkbutton(main_frame, text="🍬 Sugar", variable=sugar_var,
               font=("Arial", 10), bg="#f5deb3", 
               activebackground="#f5deb3").pack(anchor="w", padx=40)

tk.Checkbutton(main_frame, text="🥛 Milk", variable=milk_var,
               font=("Arial", 10), bg="#f5deb3",
               activebackground="#f5deb3").pack(anchor="w", padx=40)

tk.Checkbutton(main_frame, text="🍦 Cream", variable=cream_var,
               font=("Arial", 10), bg="#f5deb3",
               activebackground="#f5deb3").pack(anchor="w", padx=40)

tk.Checkbutton(main_frame, text="🌿 Vanilla", variable=vanilla_var,
               font=("Arial", 10), bg="#f5deb3",
               activebackground="#f5deb3").pack(anchor="w", padx=40)

# Buttons frame
button_frame = tk.Frame(root, bg="#6f4e37")
button_frame.pack(pady=15)

order_btn = tk.Button(button_frame, text="Place Order", 
                      command=place_order,
                      font=("Arial", 11, "bold"), 
                      bg="#8B4513", fg="white", 
                      padx=20, pady=10, cursor="hand2")
order_btn.pack(side="left", padx=5)

payment_btn = tk.Button(button_frame, text="💳 Payment", 
                        command=handle_payment,
                        font=("Arial", 11, "bold"), 
                        bg="#4CAF50", fg="white", 
                        padx=20, pady=10, cursor="hand2")
payment_btn.pack(side="left", padx=5)

root.mainloop()