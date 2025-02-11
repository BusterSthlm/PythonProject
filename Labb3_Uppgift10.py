from tkinter import messagebox, simpledialog

def FeetToInches_Main():
    FeetToInches_Output(FeetToInches_Input())

def FeetToInches_Input():
    return simpledialog.askfloat("Feet", "Hur många Feet vill du converta till Inches?")

def FeetToInches_Output(feet=0.0):
    messagebox.showinfo("Feet to Inches",f"Du har selectat hur många kilometer du valt som är {feet} och uträkningen för detta till miles är detta:\n{feet_to_inches(feet):.2f}={feet}*12")

def feet_to_inches(feet=0.0):
    return feet*12

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 10", "Du har valt Uppgift 10 som handlar om Feet to Inches!")
    try:
        FeetToInches_Main()
    except TypeError:
        pass
    except ValueError:
        pass