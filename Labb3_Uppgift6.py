from tkinter import messagebox, simpledialog

#Uppgift 6 Calories from Fat and Carbohydrates

def input_gram_fat():
    return simpledialog.askfloat("fråga", "Hur många gram fett har du blivit av med på senaste året")

def input_gram_carbonhydrate():
    return simpledialog.askfloat("fråga","Hur många gram kolhydrater har du blivit av med på senaste året")

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
    visar_svar(input_gram_fat(),input_gram_carbonhydrate())

#Ant