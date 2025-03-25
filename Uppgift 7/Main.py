import tkinter as tk
import GUI_Class as gui
import json
import os

# Global
fontfamily = ["Helvetica", "Verdana", "Times New Roman"]
root_size = gui.Gui_interface()
MainFrame = tk.Frame(root_size.get_root(), padx=5,pady=10)  # framen gör så det blir inget att flyta plats med varandra
# Global

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
    functionFrame("yellow")

def Buttons(root):
    comandsPrompt=[add_new_font,seach_fonts,edit_font,remove_font,exit]
    namePrompt=["Nytt typsnitt\n(skapa Upp)","Sök typsnitt\n(läs)","Redigera typsnitt\n(uppdatera)","Ta bort\n(radera)","Avsluta programet\n(stänga av)"]
    # Lägg till ,command=comandsPrompt[i-1] när färdig med funktonerna
    for i in range(1, 6):  # skapar knappar och soclar ut också komando för varje funtion som fins i listan ovanför
        button = tk.Button(root, text=namePrompt[i-1], width=14)
        button.grid(row=i, column=2, pady=13, padx=40)
        button.configure(command=comandsPrompt[i - 1])

def functionFrame(colors):
    Frame = tk.Frame(MainFrame)
    Frame.config(background=colors, width=385, height=480)
    Frame.grid(row=2, column=3, padx=5)
    return Frame

def descriptions_text(text_Insering,frame,colors):
    count=0
    for text in text_Insering:
        text_intreduction = tk.Label(frame, text=text)
        text_intreduction.config(background=colors)
        text_intreduction.grid(row=count, column=2-count,padx=5,pady=5)
        count+=1

def textArea(frame):
    text_contener = tk.Text(frame, width=36, height=10, borderwidth=1, relief="solid")
    text_contener.grid(row=5, column=2, pady=10, padx=10)
    return text_contener

# Skapa upp - Create
def add_new_font():
    frame=functionFrame("red")
    descriptions_text(["Lägg till fonts","Font namn:"],frame,"red")
    text_contener=textArea(frame)
    add_entry=tk.Entry(frame,width=40)
    add_entry.config(borderwidth=1, relief="solid")
    add_entry.grid(row=1,column=2,pady=5,padx=5)
    add_fonts=tk.Button(frame,text="Lägg till",command=lambda : add_font(add_entry,text_contener))
    add_fonts.config(borderwidth=2,relief="solid")
    add_fonts.grid(row=2,column=2,pady=5,padx=5)


def add_font(new_font,text_contener):
    fontfamily.append(new_font.get())#behöver en text här i ()
    text_contener.insert(1.0,f"Du har lagt till {new_font.get()} i listan!\n")

def seach_fonts():
    frame=functionFrame("purple")
    descriptions_text(["Sök efter fonts","söker efter:"],frame,"purple")
    text_contener = textArea(frame)
    Seach_entry=tk.Entry(frame,width=40)
    Seach_entry.config(borderwidth=1, relief="solid")
    Seach_entry.grid(row=1,column=2,pady=5,padx=5)
    Seach_fonts=tk.Button(frame,text="Lägg till",command=lambda : seach_font(Seach_entry,text_contener))
    Seach_fonts.config(borderwidth=2,relief="solid")
    Seach_fonts.grid(row=2,column=2,pady=5,padx=5)

def seach_font(name,text_contener):
    for fonts in fontfamily:  # Söker igenom lista
        if name.get() == fonts:
            text_contener.insert(1.0, f"{name.get()} fonten\nfins här i listan!\n")

def edit_font():
    functionFrame("pink")

def remove_font():
    functionFrame("gray")
    fontfamily.clear()





if __name__ == '__main__':
    main()