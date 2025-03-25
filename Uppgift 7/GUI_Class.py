import tkinter as tk
class Gui_interface:
    def __init__(self):
        self.__root = tk.Tk()
        self.__size = "600x500"


    def get_size(self):
        return self.__size

    def get_root(self):
        return self.__root