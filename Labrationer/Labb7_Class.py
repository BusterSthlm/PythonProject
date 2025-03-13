import tkinter as tk
class GUI:
    def __init__(self,bools=False):
        self.__root = tk.Tk()
        self.__bools = bools

    def get_root(self):
        return self.__root


    def get_bools(self):
        return self.__bools

    def set_bools(self,setBool):
        self.__bools = setBool