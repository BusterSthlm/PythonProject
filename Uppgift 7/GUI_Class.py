import tkinter as tk
class Gui_interface:
    def __init__(self):
        self.__root = tk.Tk()
        self.__ID = "typsnitt"
        self.__IDNumber = 3
        self.__dict = {"typsnitt1":"Helvetica","typsnitt2": "Verdana"}
# ID För typsnittet
    def get_Id(self):
        return self.__ID
    #Nummer kopplat till iD. Varja font får var sitt nummer
    def get_IdNumber(self):
        return self.__IDNumber
    def set_IDNumber(self,number):
        self.__IDNumber+=number
    #skapa en Dictionatary
    def get_dict(self):
        return self.__dict
    #Skriv till dict
    def set_dict(self,dicts):
        self.__dict = dicts
    # Skapar Root GUI
    def get_root(self):
        return self.__root

    def __str__(self):
        message =""
        for messages in self.__dict.values(): #loopar igenom dictonary o skapar en sträng
            message=message+f"{messages} finns sparad i dictanary!\n{"-"*36}\n"
        return f"{message}"