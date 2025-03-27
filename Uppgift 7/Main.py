import tkinter as tk
import GUI_Class as gui

# Global
font_root = gui.Gui_interface()
MainFrame = tk.Frame(font_root.get_root(), padx=5,pady=10)  # framen gör så det blir inget att flyta plats med varandra
# Global

###############################################################################################################

# Main funktionerna
def main():
    GUI_interface()
    font_root.get_root().mainloop()

def GUI_interface():
    font_root.get_root().title("Uppgift 7")
    font_root.get_root().config(background="#6082B6")
    font_root.get_root().geometry("680x500")

    MainFrame.config(background="#6082B6", width=640, height=500)
    MainFrame.grid(row=0, column=0)

    buttonFrame = tk.Frame(MainFrame)
    buttonFrame.config(background="Steel Blue",width=185,height=480,borderwidth=2,relief="sunken")
    buttonFrame.grid(row=2,column=1,padx=5)

    MainText = tk.Label(buttonFrame)
    MainText.config(text="Typsnitt",font=10,background="Steel Blue")
    MainText.grid(row=0, column=2,padx=5,pady=10)

    Buttons(buttonFrame)

    function_Frame_placement=functionFrame("#6082B6")
    function_Frame_placement.grid(padx=10)

def Buttons(root):
    comandsPrompt=[add_new_font,print_fonts,edit_font,remove_font,exit]
    namePrompt=["Nytt typsnitt\n(skapa Upp)","skriv ut all typsnitt\n(läs)","Redigera typsnitt\n(uppdatera)","Ta bort typsnitt\n(radera)","Avsluta programet\n(stänga av)"]
    # Lägg till ,command=comandsPrompt[i-1] när färdig med funktonerna
    for i in range(1, 6):  # skapar knappar och soclar ut också komando för varje funtion som fins i listan ovanför
        button = tk.Button(root, text=namePrompt[i-1], width=14)
        button.grid(row=i, column=2, pady=13, padx=40)
        button.configure(command=comandsPrompt[i - 1],background="#6082B6", borderwidth=2,relief="ridge")

def functionFrame(colors):
    Frame = tk.Frame(MainFrame)#skapar frames som används hela applications gång
    Frame.config(background=colors, width=440, height=480)
    Frame.grid(row=2, column=3, padx=5)
    return Frame

def descriptions_text(text_Insering,frame,colors):
    count=0
    for text in text_Insering:#skapar labels som lägg tills när det funktioner vill ha det
        #skaper positioner för texten när vi lägger till dom
        text_intreduction = tk.Label(frame, text=text)
        text_intreduction.config(background=colors)
        if count == 0:
            text_intreduction.grid(row=count, column=2-count,padx=5,pady=5)
        else:
            text_intreduction.grid(row=count, column=1, padx=5, pady=5)
        count+=1

def textArea(frame):
    #text area där sickas in resultatet från vi sickar ut till användaren
    text_contener = tk.Text(frame, width=36, height=10, borderwidth=1, relief="solid")#skapar en text area som vi kan använda oss av i funktionerna
    text_contener.grid(row=5, column=2, pady=10, padx=10)
    return text_contener
###############################################################################################################




# Skapa upp - Create
def add_new_font():
    #första grejerna som läggs till i början
    functionFrame("#6082B6") #skapar frame för att gömma tidigare funktioner
    frame=functionFrame("Steel blue") #skapar frame för denna funktionen
    frame.config(borderwidth=2, relief="sunken")
    descriptions_text(["Lägg till typsnitt","typsnitt namn:"],frame,"Steel blue")    #skappar label texter till funktionen
    text_contener=textArea(frame)#skapar en text area för all out put
    text_contener.insert(1.0,"Skriv in ett typsnitt namn!\n")
    #skapar entrys och knappar
    add_entry=tk.Entry(frame,width=40)
    add_entry.config(borderwidth=1, relief="solid")
    add_entry.grid(row=1,column=2,pady=5,padx=5)

    add_fonts=tk.Button(frame,text="Lägg till",command=lambda : add_font(add_entry.get(),text_contener))#knapp som sickar oss vidare till funktionen nedan för
    add_fonts.config(background="#6082B6", borderwidth=2,relief="ridge")
    add_fonts.grid(row=2,column=2,pady=5,padx=5)


def add_font(new_font,text_contener):
    font_dict=font_root.get_dict()
    cheacking_dict_font=False
    for font_names in font_root.get_dict().values():
        if font_names == new_font:
            cheacking_dict_font=True
    if cheacking_dict_font:
        text_contener.insert(1.0, f"{new_font} finns redan i listan!\n")
    else:
        IdKey=f"{font_root.get_IdNumber()}"
        font_root.set_IDNumber(1)
        key=f"{font_root.get_Id()+IdKey}"
        font_dict[key]=new_font
        font_root.set_dict(font_dict)
        text_contener.insert(1.0,f"Du har lagt till {new_font} i listan!\n")

###############################################################################################################




# Skriv ut - Read
def print_fonts():
    # första grejerna som läggs till i början
    functionFrame("#6082B6")#skapar frame för att gömma tidigare funktioner
    frame=functionFrame("Steel blue")#skapar frame för denna funktionen
    frame.config(borderwidth=2, relief="sunken")
    descriptions_text(["Skriv ut all typsnitt"],frame,"Steel blue")#skappar label texter till funktionen
    text_contener = textArea(frame) #skapar en text area för all out put
    text_contener.insert(1.0, str(font_root))#Sickar ut all info om fonterna
###############################################################################################################



# Edit - Update
def edit_font():
    # första grejerna som läggs till i början
    functionFrame("#6082B6")#skapar frame för att gömma tidigare funktioner
    frame=functionFrame("Steel blue")#skapar frame för denna funktionen
    frame.config(borderwidth=2, relief="sunken")
    descriptions_text(["Redigera en typsnitt", "Gammla typsnitt:","Nytt typsnitt:"], frame, "Steel blue")#skappar label texter till funktionen
    text_contener = textArea(frame)#skapar en text area för all out put
    text_contener.insert(1.0, "Redigera ett typsnitt namn!\n")
    #skapar entrys och knappar
    oldfont_entry = tk.Entry(frame, width=40)
    oldfont_entry.config(borderwidth=1, relief="solid")
    oldfont_entry.grid(row=1, column=2, pady=5, padx=5)

    newfont_entry = tk.Entry(frame, width=40)
    newfont_entry.config(borderwidth=1, relief="solid")
    newfont_entry.grid(row=2, column=2, pady=5, padx=5)

    edit_fonts_button = tk.Button(frame, text="Edit typsnitt", command=lambda: editing_font(newfont_entry.get(),oldfont_entry.get(), text_contener))
    edit_fonts_button.config(background="#6082B6", borderwidth=2,relief="ridge")
    edit_fonts_button.grid(row=3, column=2, pady=5, padx=5)

def editing_font(new_name,old_name,text_contener):
    edit_cheack=True
    for font_keys,font_names in font_root.get_dict().items():# Om listan finns byter den ut namnet med ett nytt
        if font_names == old_name:
            font_dict=font_root.get_dict()
            font_dict[font_keys]=new_name
            text_contener.insert(1.0,f'typsnitt {old_name} ändrad till {new_name}!\n')
            edit_cheack=False
    if edit_cheack:
        text_contener.insert(1.0,f'typsnitt {old_name} finns inte i dictanaryin!\n')
###############################################################################################################



# Ta bort - Delete
def remove_font():
    functionFrame("#6082B6")#skapar frame för att gömma tidigare funktioner
    frame=functionFrame("Steel blue")#skapar frame för denna funktionen
    frame.config(borderwidth=2, relief="sunken")
    descriptions_text(["Ta bort en typsnitt", "typsnitt Namn:"], frame, "Steel blue")#skappar label texter till funktionen
    text_contener = textArea(frame)#skapar en text area för all out put
    text_contener.insert(1.0, "Ta bort ett typsnitt namn!\n")
    # skapar entrys och knappar
    entry_remove_font = tk.Entry(frame,width=40)
    entry_remove_font.config(borderwidth=1, relief="solid")
    entry_remove_font.grid(row=1, column=2, pady=5, padx=5)

    remove_fonts_button = tk.Button(frame, text="Ta bort",command=lambda: removing_font(entry_remove_font.get(),text_contener))
    remove_fonts_button.config(background="#6082B6", borderwidth=2,relief="ridge")
    remove_fonts_button.grid(row=3, column=2, pady=5, padx=5)

def removing_font(remove_font,text_contener):
    remove_cheack=True
    remove_key=""
    for remove_font_key,remove_font_name in font_root.get_dict().items():
        if remove_font_name == remove_font:
            remove_key=remove_font_key
            text_contener.insert(1.0,f'Typsnitt {remove_font} har tagits bort!\n')
            remove_cheack=False
    if remove_cheack:
        text_contener.insert(1.0,f'Typsnitt {remove_font} finns inte i listan!\n')
    else:
        font_dict = font_root.get_dict()
        font_dict.pop(remove_key)
        font_root.set_IDNumber(-1)
###############################################################################################################


if __name__ == '__main__':
    main()