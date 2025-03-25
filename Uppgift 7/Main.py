import tkinter as tk
import GUI_Class as gui

root_size = gui.Gui_interface()
MainFrame = tk.Frame(root_size.get_root(), padx=5,pady=10)  # framen gör så det blir inget att flyta plats med varandra

def main():
    GUI_interface()
    root_size.get_root().mainloop()

def GUI_interface():
    root_size.get_root().title("Uppgift 7")
    root_size.get_root().config(background="White")
    root_size.get_root().geometry(root_size.get_size())
    MainFrame.config(background="green", width=600, height=500)
    MainFrame.grid(row=0, column=0)
    buttonFrame = tk.Frame(MainFrame)
    buttonFrame.config(background="blue",width=185,height=480)
    buttonFrame.grid(row=2,column=1,padx=5)
    MainText = tk.Label(buttonFrame)
    MainText.config(text="Typsnitt",font=10)
    MainText.grid(row=0, column=2,padx=5,pady=10)
    Buttons(buttonFrame)
    functionFrame("green")

def Buttons(root):
    comandsPrompt=[creating,seaching,updating,deleteItem]
    namePrompt=["Nytt typsnitt\n(skapa Upp)","Sök typsnitt\n(läs)","Redigera typsnitt\n(uppdatera)","Ta bort\n(radera)"]
    # Lägg till ,command=comandsPrompt[i-1] när färdig med funktonerna
    for i in range(1, 5):  # skapar knappar och soclar ut också komando för varje funtion som fins i listan ovanför
        button = tk.Button(root, text=namePrompt[i-1], width=14)
        button.grid(row=i, column=2, pady=13, padx=40)
        button.configure(command=comandsPrompt[i - 1])

def functionFrame(colors):
    Frame = tk.Frame(MainFrame)
    Frame.config(background=colors, width=385, height=480)
    Frame.grid(row=2, column=3, padx=5)
    return Frame

def creating():
    functionFrame("red")

def seaching():
    functionFrame("purple")

def updating():
    functionFrame("pink")

def deleteItem():
    functionFrame("gray")

if __name__ == '__main__':
    main()