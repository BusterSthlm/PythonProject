from tkinter import messagebox, simpledialog
from Labb3_uppgift7 import total_value

#Uppgift 6 Calories from Fat and Carbohydrates


# Beräkna kalorier från fett
def calories_from_fat(gram_fat):
    return gram_fat * 9

# beräkna kalorier från kolhydrater
def calories_from_carbonhydrates(gram_carbonhydrate):
    return gram_carbonhydrate * 9

def visar_svar(gram_fat,gram_carbonhydrate):
    all_cals = calories_from_fat(gram_fat)
    all_carbs = calories_from_carbonhydrates(gram_carbonhydrate)

    total_value = all_cals + all_carbs

    messagebox.showinfo("Titel",f"Totala kalorier: {total_value} kalorier")


#Frågorna till användarna

if __name__ == "__main__":
    gram_fat = simpledialog.askfloat("fråga", "Hur många gram fett har du blivit av med på senaste året")
    gram_carbonhydrate = simpledialog.askfloat("fråga", "Hur många gram kolhydrater har du blivit av med på senaste året")
    visar_svar(gram_fat,gram_carbonhydrate)

#Ant