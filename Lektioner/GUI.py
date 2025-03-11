import tkinter as tk


root = tk.Tk()
root.title('Mitt första GUI')
root.geometry("400x300")

label = tk.Label(root,text = "Välkommen ill Tkinter ")
label.pack()

root.mainloop()