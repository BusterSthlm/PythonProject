import tkinter as tk
class Gui_interface:
    def __init__(self):
        self.__root = tk.Tk()
        self.__ID = "typsnitt"
        self.__IDNumber = 3
        self.__dict = {"typsnitt1":"Helvetica","typsnitt2": "Verdana"}

    def get_Id(self):
        return self.__ID

    def get_IdNumber(self):
        return self.__IDNumber
    def set_IDNumber(self,number):
        self.__IDNumber+=number

    def get_dict(self):
        return self.__dict

    def set_dict(self,dicts):
        self.__dict = dicts

    def get_root(self):
        return self.__root

    def __str__(self):
        message =""
        for messages in self.__dict.values():
            message=message+f"{messages} finns sparad i dictanary!\n{"-"*36}\n"
        return f"{message}"