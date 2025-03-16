from tkinter import *
from tkinter import ttk

class Gui(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        initframe = ttk.Frame(self, padding="3 3 12 12")
        initframe.grid(column=0, row=0, sticky=(N, W, E, S))
        initframe.columnconfigure(0, weight=1)
        initframe.rowconfigure(0, weight=1)
        self.resizable(False, False)


        ttk.Button(initframe, text="Check Info", command=self.check_info).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(initframe, text="Run Tests" ).grid(column=4, row=2, sticky=(W, E))

        for child in initframe.winfo_children():
            child.grid_configure(padx=20, pady=20)

        self.update()
        self.geometry(self.geometry())

        self.bind('<Return>', self.check_info_enter)

    def goback(self):
        self.destroy()

    def check_info(self):
        info_frame = ttk.Frame(self, padding="3 3 12 12")
        info_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        info_frame.columnconfigure(0, weight=1)
        info_frame.rowconfigure(0, weight=1)
        self.resizable(False, False)

        ttk.Button(info_frame, text="Return Home", command=self.goback).grid(column=2, row=2, sticky=(W, E))


    def check_info_enter(self, event):
        self.update()



if __name__ == "__main__":
    app = Gui(None)
    app.title('Initial')
    app.mainloop()