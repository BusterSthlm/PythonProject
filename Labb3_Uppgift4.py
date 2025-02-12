
from tkinter import messagebox, simpledialog

# funktion som hämtar svaren från användaren
def replacement_cost():
    return simpledialog.askfloat(" Question","Skriv in totala kostnaden för ersättning av byggnaden: ")

# Beräknar kostnaden med användarens svar
def calculation(price):
    return price * 0.8

# skriva ut den nya kostnaden.
def show_new_price(price):
   return messagebox.showinfo("Fråga", f" Ditt nya pris är: {calculation(price):.2f}")

if __name__ == "__main__":
    show_new_price(replacement_cost())






