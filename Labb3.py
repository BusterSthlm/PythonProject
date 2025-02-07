from enum import Enum
from tkinter import messagebox, simpledialog

class MenyVal(Enum):
    Uppgift_1 = 1
    Uppgift_2 = 2
    Uppgift_3 = 3
    Uppgift_4 = 4
    Uppgift_5 = 5
    Uppgift_6 = 6
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

        if choice == MenyVal.Uppgift_1.value:
            Uppgift = simpledialog.askfloat("Area","Ange radie: ")
        elif choice == MenyVal.Uppgift_2.value:
            Uppgift = simpledialog.askfloat("Area längd","Ange längd: ")
        elif choice == MenyVal.Uppgift_3.value:
            Uppgift = simpledialog.askfloat("Area bas", "Ange bas: ")
        elif choice == MenyVal.Uppgift_4.value:
            Uppgift = simpledialog.askfloat("Area Sida","Ange sida: ")
        elif choice == MenyVal.Uppgift_5.value:
            Uppgift = simpledialog.askfloat("Area Sida", "Ange sida: ")
        elif choice == MenyVal.Uppgift_6.value:
            Uppgift = simpledialog.askfloat("Area Sida","Ange sida: ")
        elif choice == MenyVal.AVSLUTA.value:
            messagebox.showinfo("Ending", "Avslutar programmet.")
            break
        else:
            messagebox.showerror("Error","Ogiltigt val, försök igen.")



if __name__ == "__main__":
    main()