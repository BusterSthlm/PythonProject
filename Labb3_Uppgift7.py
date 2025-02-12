from enum import Enum
from tkinter import messagebox, simpledialog

# Stadium seating
"""
There are three seating categories at a stadium.
Class A seats cost $20,
Class B seats cost $15,
and Class C seats cost $10.

Write a program that asks how many tickets for each class of seats
were sold, then displays the amount of income generated from ticket sales.
"""
total_value = 0  # Defining total_value at the beginning


class SeatingCost(Enum):
    CLASS_A = 20
    CLASS_B = 15
    CLASS_C = 10


# Function to ask how many tickets were sold for each class
def tickets():
    class_a_tickets = simpledialog.askinteger("Fråga", "Hur många biljetter har kategori A sålt?")
    class_b_tickets = simpledialog.askinteger("Fråga", "Hur många biljetter har kategori B sålt??")
    class_c_tickets = simpledialog.askinteger("Fråga", "Hur många biljetter har kategori C  sålt??")
    return class_a_tickets, class_b_tickets, class_c_tickets

# Function to calculate the total income from ticket sales
def sold_tickets(class_a_tickets, class_b_tickets, class_c_tickets):
    global total_value  # Make sure to use the global variable `total_value`

    # Calculate total income for each class
    total_value += class_a_tickets * SeatingCost.CLASS_A.value
    total_value += class_b_tickets * SeatingCost.CLASS_B.value
    total_value += class_c_tickets * SeatingCost.CLASS_C.value


# Main program execution
def main():
    class_a_tickets, class_b_tickets, class_c_tickets = tickets()  # Get the number of tickets sold
    sold_tickets(class_a_tickets, class_b_tickets, class_c_tickets)  # Calculate total income

    # Display the total income
    messagebox.showinfo("Inkomst", f"Total income from ticket sales: ${total_value}")


if __name__ == '__main__':
    main()