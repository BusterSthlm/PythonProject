from tkinter import messagebox, simpledialog

def FeetToInches_Main():
    FeetToInches_Output(FeetToInches_Input())#sickar en för frågan till inputen om feet till outputens reqest

def FeetToInches_Input():
    return simpledialog.askfloat("Feet", "Hur många Feet vill du converta till Inches?")#frågar hur många feet som ska conventeras till Inches

def FeetToInches_Output(feet=0.0):
    #Sickar ut all info till usern och också sickar en matte fråga till feet_to_inches för att kontrolera att det är rätt
    messagebox.showinfo("Feet to Inches",f"Du har selectat hur många kilometer du valt som är {feet} och uträkningen för detta till miles är detta:\n{feet_to_inches(feet):.2f}={feet}*12")

def feet_to_inches(feet=0.0):
    return feet*12 #matten för att komma fram till Inches

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 10", "Du har valt Uppgift 10 som handlar om Feet to Inches!")
    try:
        FeetToInches_Main()
    except TypeError:
        pass
    except ValueError:
        pass