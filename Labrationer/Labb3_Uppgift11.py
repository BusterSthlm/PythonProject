from tkinter import messagebox, simpledialog
import random

def MathQuiz_Main():
    firstNumber=Random_numbers()#skriver in ett första random nummer
    secondNumber=Random_numbers()#skriver in ett andra random nummer
    awnser = MathQuiz_Input(firstNumber, secondNumber)#användarens svar
    correctAwnser = MathQuiz_Awnser(firstNumber, secondNumber)#datorns svar
    MathQuiz_Output(int(awnser),int(correctAwnser))#slut resultat

def Random_numbers():
    return random.randint(0,500)#random nummer mellan 0-500

def MathQuiz_Input(num1=0,num2=0):
    return simpledialog.askfloat("Fråga", f"   {num1}\n+ {num2}\n\nType in your awnser here:")#frågar användaren om vad deras svar är

def MathQuiz_Awnser(num1=0.0, num2=0.0):
    return  num1+num2 #datorns rättning

def MathQuiz_Output(awnser=0,correctAwnser=0):
    if awnser == correctAwnser: #kontrolerar om användaren och datorn har kommit fram till samma svar
        Result= f"Du har löst frågan utifrån uträkningen med svaret: {awnser}!"
    else:
        Result = f"Du svarade fel på frågan och rätt svar var: {correctAwnser} mendans du svarade: {awnser}!"
    messagebox.showinfo("Math Quiz",f"{Result}")#sickar ut resultatet

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 11", "Du har valt Uppgift 11 som handlar om Math Quiz!\nSimpla Matte frågot vill bli stälda!")
    try:
        MathQuiz_Main()
    except TypeError:
        pass
    except ValueError:
        pass