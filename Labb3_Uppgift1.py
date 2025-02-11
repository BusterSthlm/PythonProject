from tkinter import messagebox, simpledialog

def kilometer_Main():
    kilometer_Output(kilometer_Input())

def kilometer_Input():
    return simpledialog.askfloat("Distance", "Hur långt avstånd i km har du kört?")

def kilometer_Output(kilometers=0.0):
    messagebox.showinfo("The Kilometer Converter Problem",f"Du har selectat hur många kilometer du valt som är {kilometers} och uträkningen för detta till miles är detta:\n{kilometer(kilometers):.2f}={kilometers}*0.6214")

def kilometer(km=0.0):
    return km*0.6214

if __name__ == '__main__':
    messagebox.showinfo("Uppgift 1", "Du har valt Uppgift 1 som handlar om The kilometer converter problem!")
    try:
        kilometer_Main()
    except TypeError:
        pass
    except ValueError:
        pass