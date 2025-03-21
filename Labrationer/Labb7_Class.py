import tkinter as tk
class GUI:
    def __init__(self,bools=False):
        self.__root = tk.Tk() # Skapar vi root
        self.__bools = bools # Satt till Falskt

    def get_root(self):
        return self.__root # Hämtar rooten


    def get_bools(self):
        return self.__bools #Hämta värdet från bool

    def set_bools(self,setBool):
        self.__bools = setBool # vill sätta värdet för bool