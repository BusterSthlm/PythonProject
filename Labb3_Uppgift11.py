from tkinter import messagebox, simpledialog
import random

def MathQuiz_Awnser(num1=0.0, num2=0.0):
    return  num1+num2

def MathQuiz_Input(num1=0,num2=0):
    return simpledialog.askfloat("Fråga", f"   {num1}\n+ {num2}\n\nType in your awnser here:")

def Random_numbers():
    return random.randint(0,500)

def MathQuiz_Main():
    firstNumber=Random_numbers()
    secondNumber=Random_numbers()
    awnser = MathQuiz_Input(firstNumber, secondNumber)
    correctAwnser = MathQuiz_Awnser(firstNumber, secondNumber)
    MathQuiz_Output(int(awnser),int(correctAwnser))

def MathQuiz_Output(awnser=0,correctAwnser=0):
    if awnser == correctAwnser:
        Result= f"Du har löst frågan utifrån uträkningen med svaret: {awnser}!"
    else:
        Result = f"Du svarade fel på frågan och rätt svar var: {correctAwnser} mendans du svarade: {awnser}!"

    messagebox.showinfo("Math Quiz",f"{Result}")

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 11", "Du har valt Uppgift 11 som handlar om Math Quiz!\nSimpla Matte frågot vill bli stälda!")
    try:
        MathQuiz_Main()
    except TypeError:
        pass
    except ValueError:
        pass
