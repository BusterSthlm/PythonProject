import tkinter as tk

# Global font lista
font_dict = []

# Main
def main():
    pass

def get_menu_text(root):
    message=["1. Lägg till varor",
             "2. Söka namn på varan & printa ut all data om varan",
             "3. Skriva ut all information om alla varor",
             "4. Uppdatera antal och pris på valt vara",
             "5. Ta bort varan ifrån nyckel fårn dictionary",
             "6. Spara shopping listan I en JSON fil",
             "7. Tömma hela shoppinglistan på varor",
             "8. Visa bild på sökt vara",
             "9. Total kostnaden",
             "10. Avsluta programet"]


def add_new_font():

    font_name = entry.get().strip()  

    if font_name:
        font_dict.append(font_name)
        label.config(text=f'Font "{font_name}" har lagts till!')
    else:
        label.config(text="Skriv in ett fontnamn!")

    print("Fonts:", font_dict)

def search_font():

    search = search_entry.get().strip()  
    if search in font_dict:
        search_result.config(text=f'Font "{search}" hittades!')
    else:
        search_result.config(text=f'Font "{search}" hittades EJ!')

def edit_font():

    old_name = entry_old.get().strip() # Strip tar bort mellanrummen innan och efter.
    new_name = entry_new.get().strip()

    if old_name in font_dict: # Om listan finns byter den ut namnet med ett nytt
        index = font_dict.index(old_name)
        font_dict[index] = new_name
        label.config(text=f'Font "{old_name}" ändrad till "{new_name}"!')
    else:
        label.config(text=f'Font "{old_name}" finns EJ i listan!')

    print("Fonts:", font_dict)

def remove_font():
# 4.Ta bort fonten
    font_name = entry_remove.get().strip()
# OM namnet man skriver in finns i listan tas det bort med remove()
    if font_name in font_dict:
        font_dict.remove(font_name)
        remove_label.config(text=f'Font "{font_name}" har tagits bort!')
    else:
        remove_label.config(text=f'Font "{font_name}" finns EJ i listan!')

    print("Fonts:", font_dict)

# --------------- GUI -----------------
root = tk.Tk()
root.title("Typografihanteraren")
root.geometry("500x500")

# Skapa font
tk.Label(root, text="Lägg till en ny font:").pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Lägg till Font", command=add_new_font).pack()
label = tk.Label(root, text="")
label.pack(pady=5)

# Sök font
tk.Label(root, text="Sök efter en font:").pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)
tk.Button(root, text="Sök", command=search_font).pack()
search_result = tk.Label(root, text="")
search_result.pack(pady=5)

# Redigera fonten
tk.Label(root, text="Redigera en font:").pack()
entry_old = tk.Entry(root, width=30)
entry_old.pack(pady=5)
entry_old.insert(0, "Gammalt namn")

entry_new = tk.Entry(root, width=30)
entry_new.pack(pady=5)
entry_new.insert(0, "Nytt namn")

tk.Button(root, text="Ändra Font", command=edit_font).pack()

# Rensa listan
tk.Label(root, text="Ta bort en font:").pack()
entry_remove = tk.Entry(root, width=30)
entry_remove.pack(pady=5)
tk.Button(root, text="Ta bort Font", command=remove_font).pack()
remove_label = tk.Label(root, text="")
remove_label.pack(pady=5)

# Starta GUI
root.mainloop()