"""
#import tkinter as tk

#root = tk.Tk()
#root.title("Mitt första GUI")
#root.geometry("400x300")

#label = tk.Label(root, text="Välkommen till Tkinter!")
#label.pack()

#root.mainloop()


# Kod för GUI med knapp
#import tkinter as tk

#root = tk.Tk()
#root.title("Mitt första GUI")
#root.geometry("400x300")

#label = tk.Label(root, text="Välkommen till Tkinter!")
#label.pack()

#entry = tk.Entry(root)
#entry.pack()

#def visa_meddelande():
 #   inmatning = entry.get()
 #   print(inmatning)
 #   text_area.insert(tk.END, f'{inmatning}\n')

#button = tk.Button(root, text="Klicka här", command=visa_meddelande)
#button.pack()

#text_area = tk.Text(root, height=10, width=40)
#text_area.pack()


#root.mainloop()

# kod för gui med radiobutton och dropdownmeny
import tkinter as tk

root = tk.Tk()
root.title("Mitt första GUI")
root.geometry("400x400")
#root.configure(bg="lightblue")

label = tk.Label(root, text="Välkommen till Tkinter!")
label.pack()

entry = tk.Entry(root)
entry.pack()

val = tk.StringVar()

tk.Radiobutton(root, text="Alternativ 1", variable=val, value="1").pack()
tk.Radiobutton(root, text="Alternativ 2", variable=val, value="2").pack()

alternativ = ["Val 1", "Val 2", "Val 3"]
val = tk.StringVar()
dropdown = tk.OptionMenu(root, val, *alternativ)
dropdown.pack()


def visa_meddelande():
    inmatning = entry.get()
    print(inmatning)
    text_area.insert(tk.END, f'{inmatning}\n')

button = tk.Button(root, text="Klicka här", command=visa_meddelande)
button.pack()

text_area = tk.Text(root, height=10, width=40)
text_area.pack()


root.mainloop()


import tkinter as tk

class DictionaryApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dictionary GUI")
        self.root.geometry("400x300")
        self.data = {}

        self.label_key = tk.Label(self.root, text="Nyckel:")
        self.label_key.pack()
        self.entry_key = tk.Entry(self.root)
        self.entry_key.pack()

        self.label_value = tk.Label(self.root, text="Värde:")
        self.label_value.pack()
        self.entry_value = tk.Entry(self.root)
        self.entry_value.pack()

        self.text_area = tk.Text(self.root, height=10, width=40)
        self.text_area.pack()

        self.add_button = tk.Button(self.root, text="Lägg till", command=self.add_entry)
        self.add_button.pack()

        self.delete_button = tk.Button(self.root, text="Ta bort", command=self.delete_entry)
        self.delete_button.pack()

        self.show_button = tk.Button(self.root, text="Visa dictionary", command=self.show_dict)
        self.show_button.pack()
        self.root.mainloop()

    def add_entry(self):
        key = self.entry_key.get()
        value = self.entry_value.get()
        self.data[key] = value
        self.show_dict()

    def delete_entry(self):
        key = self.entry_key.get()
        if key in self.data:
            del self.data[key]
        self.show_dict()

    def show_dict(self):
        self.text_area.delete(1.0, tk.END)
        for key, value in self.data.items():
            self.text_area.insert(tk.END, f"{key}: {value}\n")


if __name__ == '__main__':
    app = DictionaryApp()
"""
# kod för GUI med visa bild
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title('Visa bild i Tkinter')
root.geometry('350x250')

bild = Image.open('vulkaner.png')
bild = bild.resize((300, 200))
img = ImageTk.PhotoImage(bild)  # Skapa bildobjekt

label = tk.Label(root, image=img)
label.image = img  # Behåll referens till bilden
label.pack()

root.mainloop()