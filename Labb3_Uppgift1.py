from tkinter import messagebox, simpledialog

def kilometer_Main():
    kilometer_Output(kilometer_Input())#sickar en för frågan till inputen om kilometer till outputens reqest

def kilometer_Input():
    #frågar användaren om att skriva in hur många kilometer det vill konvertera till miles
    return simpledialog.askfloat("Distans i kilometer", "Hur många kilometer vill du konvertera till miles?")

def kilometer_Output(kilometers=0.0):
    #sickar ut slut resultatet ifrån hur mycket usern ville konvertera
    messagebox.showinfo("The Kilometer Converter Problem",f"Du har selectat hur många kilometer du valt som är {kilometers} och uträkningen för detta till miles är detta:\n{kilometer(kilometers):.2f}={kilometers}*0.6214")

def kilometer(km=0.0):
    return km*0.6214 #räknar ut hur många miles det är per kilometer

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 1", "Du har valt Uppgift 1 som handlar om The kilometer converter problem!")
    try:
        kilometer_Main()
    except TypeError:
        pass
    except ValueError:
        pass