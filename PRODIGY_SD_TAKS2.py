import tkinter as tk
from tkinter import messagebox
import random

# Function to handle the betting process
def bet():
    try:
        bamt = int(entry_bet_amount.get())
        if bamt < 20:
            messagebox.showerror("Error", "MINIMUM BETTING AMOUNT IS $20")
            return
        elif bamt > money[0]:
            messagebox.showerror("Error", "YOU DON'T HAVE ENOUGH MONEY")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")
        return
    
    choice = number_choice.get()
    numb = random.randint(1, 4)
    
    if numb == choice:
        messagebox.showinfo("Congratulations!", "YOU HAVE WON THE PRIZE!")
        money[0] += bamt
    else:
        messagebox.showinfo("Bad Luck", f"OHH LUCKY NUMBER IS {numb}\nTRY NEXT TIME")
        money[0] -= bamt
    
    label_balance.config(text=f"YOUR CURRENT WALLET BALANCE IS  $ {money[0]}")
    
    if money[0] <= 0:
        messagebox.showinfo("Game Over", "YOU HAVE RUN OUT OF MONEY")
        root.quit()

# Function to add money to the wallet
def add_money():
    try:
        add_amt = int(entry_add_amount.get())
        money[0] += add_amt
        label_balance.config(text=f"YOUR CURRENT WALLET BALANCE IS  $ {money[0]}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")

# Initialize the main window
root = tk.Tk()
root.title("Betting Saga")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Initialize user's money
money = [500]

# Labels and entries for adding money
label_intro = tk.Label(root, text="~~~~~~~~~~WELCOME TO BETTING SAGA~~~~~~~~~~", bg="#f0f0f0", font=("Helvetica", 12))
label_intro.pack(pady=10)

label_bonus = tk.Label(root, text="CONGRATULATIONS! YOUR ENTRY BONUS IS $500", bg="#f0f0f0", font=("Helvetica", 12))
label_bonus.pack(pady=10)

label_balance = tk.Label(root, text=f"YOUR CURRENT WALLET BALANCE IS  $ {money[0]}", bg="#f0f0f0", font=("Helvetica", 12))
label_balance.pack(pady=10)

label_add_money = tk.Label(root, text="ENTER AMOUNT TO ADD TO WALLET", bg="#f0f0f0", font=("Helvetica", 12))
label_add_money.pack(pady=5)

entry_add_amount = tk.Entry(root, font=("Helvetica", 12))
entry_add_amount.pack(pady=5)

button_add_money = tk.Button(root, text="ADD MONEY", command=add_money, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
button_add_money.pack(pady=10)

# Entry for betting amount
label_bet_amount = tk.Label(root, text="ENTER THE BETTING AMOUNT", bg="#f0f0f0", font=("Helvetica", 12))
label_bet_amount.pack(pady=5)

entry_bet_amount = tk.Entry(root, font=("Helvetica", 12))
entry_bet_amount.pack(pady=5)

# Radio buttons for number choice
number_choice = tk.IntVar(value=1)

label_choose_number = tk.Label(root, text="CHOOSE THE NUMBER", bg="#f0f0f0", font=("Helvetica", 12))
label_choose_number.pack(pady=10)

radio_one = tk.Radiobutton(root, text="ONE", variable=number_choice, value=1, bg="#f0f0f0", font=("Helvetica", 12))
radio_two = tk.Radiobutton(root, text="TWO", variable=number_choice, value=2, bg="#f0f0f0", font=("Helvetica", 12))
radio_three = tk.Radiobutton(root, text="THREE", variable=number_choice, value=3, bg="#f0f0f0", font=("Helvetica", 12))
radio_four = tk.Radiobutton(root, text="FOUR", variable=number_choice, value=4, bg="#f0f0f0", font=("Helvetica", 12))

radio_one.pack(anchor="w")
radio_two.pack(anchor="w")
radio_three.pack(anchor="w")
radio_four.pack(anchor="w")

# Bet button
button_bet = tk.Button(root, text="PLACE BET", command=bet, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white")
button_bet.pack(pady=20)

# Start the GUI loop
root.mainloop()
