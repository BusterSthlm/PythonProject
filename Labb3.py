from tkinter import messagebox,simpledialog

###
from enum import Enum
from tkinter import messagebox, simpledialog
import Labb3_Uppgift1 as Uppgift1
import Labb3_Uppgift10 as Uppgift2
import Labb3_Uppgift11 as Uppgift3
"""import Labb3_Uppgift4 as Uppgift4
import Labb3_Uppgift6 as Uppgift5
import Labb3_Uppgift7 as Uppgift6"""


class MenyVal(Enum):
    Uppgift_1 = 1
    Uppgift_10 = 2
    Uppgift_11 = 3
    Uppgift_4 = 4
    Uppgift_6 = 5
    Uppgift_7 = 6
    AVSLUTA = 7

def print_meny():
    message="Välj en uppgift du vill see:\n"
    #print("Välj en areaberäkning:")
    for val in MenyVal:
        message = message + f"{val.value}. {val.name.capitalize()}\n" #egenskapern value och name för enum ger olika värden
    return message

def main():
    while True:
        try:
            choice = int(simpledialog.askfloat("Choice", f"{print_meny()}Välj en uppgift mellan 1-7: "))
            #choice = int(input("Ange ditt val (1-5): ")) # det är int funktionen som kastar felet att den inte kan konvertera sträng till heltal
        except ValueError:
            messagebox.showerror("Error","Ogiltig inmatning. Vänligen ange vilken uppgift du vill se mellan 1-7!")
            #print("Ogiltig inmatning. Vänligen ange en siffra mellan 1 och 5.")
            continue
        except TypeError:
            messagebox.showwarning("Warning","Du stänger av programet för du tryckte på cancel!")
            break
        try:
            if choice == MenyVal.Uppgift_1.value:
                messagebox.showinfo("Uppgift 1","Du har valt Uppgift 1 som handlar om The kilometer converter problem!")
                Uppgift1.kilometer_Output()
            elif choice == MenyVal.Uppgift_10.value:
                messagebox.askyesno("Uppgift 10","Du har valt Uppgift 10 som handlar om Feet to Inches!")
                Uppgift2.FeetToInches_Output()
            elif choice == MenyVal.Uppgift_11.value:
                messagebox.askyesno("Uppgift 11","Du har valt Uppgift 11 som handlar om Math Quiz!\nSimpla Matte frågot vill bli stälda!")
                Uppgift3.MathQuiz_Main()
            elif choice == MenyVal.Uppgift_4.value:
                Uppgift = messagebox.askyesno("Uppgift 4","Är du säker på att du vill starta Uppgift 4?")

            elif choice == MenyVal.Uppgift_6.value:
                Uppgift = messagebox.askyesno("Uppgift 6","Är du säker på att du vill starta Uppgift 5?")

            elif choice == MenyVal.Uppgift_7.value:
                Uppgift = messagebox.askyesno("Uppgift 7","Är du säker på att du vill starta Uppgift 6?")

            elif choice == MenyVal.AVSLUTA.value:
                messagebox.showinfo("Ending", "Avslutar programmet.")
                break
            else:
                messagebox.showerror("Error","Ogiltigt val, försök igen.")
        except TypeError:
            continue



if __name__ == "__main__":
    main()