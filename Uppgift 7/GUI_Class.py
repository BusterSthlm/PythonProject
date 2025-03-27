import tkinter as tk
class Gui_interface:
    def __init__(self):
        self.__root = tk.Tk() # skapar root
        self.__ID = "typsnitt" # Skapar fast ID
        self.__IDNumber = 3 # Dynamisk nyckel för fast ID
        self.__dict = {"typsnitt1":"Helvetica","typsnitt2": "Verdana"} # Directionaryn
# Ta fram ID För typsnittet
    def get_Id(self):
        return self.__ID
    #ta fram Nummer kopplat till iD. Varja font får var sitt nummer
    def get_IdNumber(self):
        return self.__IDNumber # Kollar var för ID som är tillgängligt. Ökar/minskar med set.
    def set_IDNumber(self,number):
        self.__IDNumber+=number # kopplas nummver till ID. Ökar eller minskar om det tas bort eller läggs till.
    #skapa en Dictionatary
    def get_dict(self):
        return self.__dict # Hämta directionary
    #Skriv till dict
    def set_dict(self,dicts):
        self.__dict = dicts # Skriver till directionary.
    # Skapar Root GUI
    def get_root(self):
        return self.__root # #få fram första rutan en gång.

    def __str__(self):# STR metod, Skriver ut allt i directinary
        message =""
        for messages in self.__dict.values(): #loopar igenom dictonary o skapar en sträng
            message=message+f"{messages} finns sparad i dictanary!\n{"-"*36}\n"
        return f"{message}"