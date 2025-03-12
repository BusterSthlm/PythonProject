import tkinter as gui
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.root = gui.Tk()
        self.root.title("Game")
        self.root.geometry("1920x1080")
        self.sens(1)
        self.update(self.machanics())
        self.root.mainloop()

    def update(self, pos):
        pass
    def machanics(self):
        pass
    def sens(self, senNumber):
        if senNumber == 1:
            bild = Image.open('vulkaner.png')
            bild = bild.resize((300, 400))
            img = ImageTk.PhotoImage(bild)
            return img
        if senNumber == 2:
            bild = Image.open('vulkaner.png')
            bild = bild.resize((300, 200))
            img = ImageTk.PhotoImage(bild)
            return img
        if senNumber == 3:
            bild = Image.open('vulkaner.png')
            bild = bild.resize((100, 600))
            img = ImageTk.PhotoImage(bild)
            return img
        if senNumber == 4:
            bild = Image.open('vulkaner.png')
            bild = bild.resize((900, 200))
            img = ImageTk.PhotoImage(bild)
            return img
        if senNumber == 5:
            bild = Image.open('vulkaner.png')
            bild = bild.resize((700, 800))
            img = ImageTk.PhotoImage(bild)
            return img
    def player(self):
        player_obj = Image.open('player.png')
        player_obj = player_obj.resize((324,450))
        return ImageTk.PhotoImage(player_obj)
    def buttons(self,senRequest):
        self.button = gui.Button(self.root, text="Klicka här", command=self.senRequest)
        return self.button.pack()
    def inputs(self):
        label = gui.Label(self.root, text=f"Pick a Level 1-3")
        return label.pack()


if __name__ == '__main__':
    App()