
"""
BESKRIVNING AV UPPGIFT 7
Typografihanterare:
 Bygg en app för att organisera och visa olika typsnitt.
    Skapa upp, Läs,uppdatera , ta bort typsnitt


"""

import tkinter as tk
import json
import os
from tkinter import messagebox, simpledialog

from Labrationer.Labb3 import print_meny
# Global
# Global
fontfamily =[]

def main():
    fonts_list = [Helvetica,Verdana,Times_New_Roman]



def get_menu_text(root):
    Meny = ["1. Skapa typsnitt",
             "2. Sök efter typsnitt",
             "3. Redigera typsnitt",
             "4. Ta bort typsnitt",
             "5. Avsluta programet"]

    pass

# Skapa upp - Create
def add_new_font():

    font.append()
    print("Din font har lagts till i listan")
    pass

# Sök - read
def search_font():
        items = groceries
        item_name = str(input("Vilken font söker du? "))
        for item in items: # Söker igenom lista
            if name.get() == item.get_name():
                print(item)


# Redigera
def edit_font():

    pass

# Ta bort
def remove_font():
    fonts_list.clear()



# spara JSon i Directionary Som tidigare.
