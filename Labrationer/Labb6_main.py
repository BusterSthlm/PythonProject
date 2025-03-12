import Labb6_Class as cart
import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage


#Main funktionen och körningen________________________________________________________________________________________________________________
def main():
    #bool för att vlja om du vill köra i consolen eller messagebox
    screen_pick = messagebox.askyesno("Console","vilken Konsol vill du använda:\nJa: Messagebox\nNej: Konsolen")
    #tre första varorna läggs till
    shop_item1 = cart.Shopping_item("Ketchup", 3, 250)
    shop_item2 = cart.Shopping_item("Äpple", 20, 180)
    shop_item3 = cart.Shopping_item("Mjölk", 2, 100)
    #list of the item shop
    shop_list=[shop_item1,shop_item2,shop_item3]
    while True:
        try:
            match get_choice(screen_pick):
                case 1:
                    shop_list.append(shoping_Item(screen_pick))
                case 2:
                    render_shoping_list(screen_pick,shop_list)
                case 3:
                    item_info(screen_pick,shop_list)
                case 4:
                    render_item_name(screen_pick,shop_list)
                case 5:
                    render_all_item_info(screen_pick,shop_list)
                case 6:
                    change_item_choice(screen_pick,shop_list)
                case 7:
                    remove_item_by_name_or_id(screen_pick,shop_list)
                case 8:
                    empty_shopping_list()
                    pass
                case 9:
                    show_product_img()
                    pass
                case 10:
                    calculate_total_price_per_product()
                    pass
                case 11:
                    program_render_ending(screen_pick)
                    break
        except KeyboardInterrupt:
            pass




#7. Ta bort items ur listan______________________________________________________________________________________________________________________
def remove_item_by_name_or_id(screen_pick,shop_list):
    count=0
    total_list=0
    for list_count in shop_list:
        count+=1
        total_list = count
    if screen_pick:
        choice=messagebox.askyesno("Namn eller Index", "Välj ja eller nej om du vill skriva in namn eller Index positionen du vill ta bort ur listan:\nJa: Namn\nNej: Index")
        if choice:
            name = simpledialog.askstring("Namn", "Vilket namn vill du ta bort?")
            count=0
            for list_item in shop_list:
                if name == list_item.get_name():
                    del shop_list[count]
                count+=1
        else:
            index = int(simpledialog.askfloat("Index",f"Vilken varas position vill du ta bort 1-{total_list}?"))
            if index == 0:
                index = 1
            del shop_list[index-1]
    else:
        choice = str(input("skriv ja eller nej om du vill skriva in namn eller Index positionen du vill ta bort ur listan:\nJa: Namn\nNej: Index\n"))
        if choice == 'Ja':
            name = str(input("Vilket namn vill du ta bort?"))
            count = 0
            for list_item in shop_list:
                if name == list_item.get_name():
                    del shop_list[count]
                count += 1
        elif choice == 'Nej':
            index = int(input(f"Vilken varas position vill du ta bort 1-{total_list}?\n"))
            if index == 0:
                index = 1
            del shop_list[index-1]
        else:
            print("Fel input Skriv Ja eller Nej För att kunna välja mellan att ta bort items")
#Ändra värdet på varor________________________________________________________________________________________________________________________
def change_item_choice(screen_pick,shop_list):
    if screen_pick:
        item_name = simpledialog.askstring("Item", "Skriv in ett namn ifrån shoping listan och ändra informationen på produkten: ")
        for list_item in shop_list:
            if item_name == list_item.get_name():
                list_item.set_count(int(simpledialog.askfloat("Antal","Hur många av den här produkten vill du ha?")))
                list_item.set_price(int(simpledialog.askfloat("Priset","Hur mycket kostar produkten vill du ha nu?")))
                messagebox.showinfo("Information",f"Namn valt: {list_item.get_name()}\n\nNya informationen:\nAntal: {list_item.get_count()}\nPriset: {list_item.get_price()}")
    else:
        item_name = str(input("Skriv in ett namn ifrån shoping listan och få all info om produkten: "))
        for list_item in shop_list:
            if item_name == list_item.get_name():
                list_item.set_count(int(input("Hur många av den här produkten vill du ha?\n")))
                list_item.set_price(int(input("Hur mycket kostar produkten vill du ha nu?\n")))
                print(f"Namn valt: {list_item.get_name()}\n\nNya informationen:\nAntal: {list_item.get_count()}\nPriset: {list_item.get_price()}\n\n")
#Renderar listan ut på skärmen________________________________________________________________________________________________________________
def render_shoping_list(screen_pick,shop_list):
    if screen_pick:
        return messagebox.showinfo("Items",f"Detta är hur många items du har i din lista: {len(shop_list)}")
    else:
        return print(f"Detta är hur många items du har i din lista: {len(shop_list)}\n")
#renderar ut listans info________________
def item_info(screen_pick,shop_list):
    if screen_pick:
        item_name = simpledialog.askstring("Item", "Skriv in ett namn ifrån shoping listan och få all info om produkten: ")
        for list_item in shop_list:
            if item_name == list_item.get_name():
                messagebox.showinfo("List",f"Namn valt: {list_item.get_name()}\n\nAntal: {list_item.get_count()}\nPriset: {list_item.get_price()}")
    else:
        item_name = str(input("Skriv in ett namn ifrån shoping listan och få all info om produkten: "))
        for list_item in shop_list:
            if item_name == list_item.get_name():
                print(f"Namn valt: {list_item.get_name()}\n\nAntal: {list_item.get_count()}\nPriset: {list_item.get_price()}\n\n")
#Renderar ut alla namn i shop listan_____
def render_item_name(screen_pick,shop_list):
    total_list_name=""
    for item_name in shop_list:
        total_list_name=total_list_name + item_name.get_name() + "\n"
    if screen_pick:
        messagebox.showinfo("Varor namn", f"Här ser du alla varors namn:\n{total_list_name}")
    else:
        print(f"Här ser du alla varors namn:\n{total_list_name}")
#Rendera ut all data om alla prudkter____
def render_all_item_info(screen_pick,shop_list):
    total_info = ""
    for items in shop_list:
        total_info = total_info + f"{'-'*20}\nNamn: " + items.get_name() +"\nAntal: "+ str(items.get_count()) +"st\nPrise: "+ str(items.get_price()) +"kr\n"
    if screen_pick:
        messagebox.showinfo("All information",f"Här är all information om alla items:\n{total_info}")
    else:
        print(f"Här är all information om alla items:\n{total_info}")
# 1. Add items____________________________________________________________________________________________________________________________________
def shoping_Item(screen_pick):
    name=""
    count=0
    price=0
    if screen_pick:
        name=simpledialog.askstring("Varan","Vad heter varan du har valt?")
        count=int(simpledialog.askfloat("Varan","Hur många antal av varan har du valt?"))
        price=int(simpledialog.askfloat("Varan","Hur mycket kostar varan?"))
    else:
        name = input("Vad heter varan du har valt?\n")
        count = int(input("\nHur många antal av varan har du valt?\n"))
        price = int(input("\nHur mycket kostar varan?\n"))
    complited_list=cart.Shopping_item(name,count,price)
    return complited_list
#meny listan__________________________________________________________________________________________________________________________________
def get_choice(screen_pick):
    try:
        if screen_pick:
            choice = int(simpledialog.askfloat("Val",f"Skriv ett nummer du i från denna lista:\n\n{render_menu_list(menu_list())}"))
        else:
            choice = int(input(f"\n\nSkriv ett nummer du i från denna lista:\n\n{render_menu_list(menu_list())}"))
    except ValueError:
        choice=11
    except TypeError:
        choice = 11
    return choice
def menu_list():
    menu=("1. Lägg till i varor:\n\n",
          "2. skriv ut alla varor element:\n\n",
          "3. Välj en vara och sicka ut all info om varan:\n\n",
          "4. Skriv ut hur många varor du har valt:\n\n",
          "5. Skriv ut alla varor i shoping korgen:\n\n",
          "6. Uppdatera antal och price på vald prudukt:\n\n",
          "7. Ta bort varan baserat på position eller namn i listan:\n\n",
          "8. Ta bort hela listan:\n\n",
          "9. Visa bild påå sökt vara:\n\n",
          "10. Uträkning på totala kostnaden av prudukten:\n\n",
          "11. Avsluta programet:\n")
    return menu
def render_menu_list(menu):
    messege=""
    for list in menu:
        messege+=list
    return messege

# 8.Rensar hela shopping listan
def empty_shopping_list(shop_list):
    shop_list.clear()
# 9. Via produkt bild
def show_product_img():
    # Skapat fönster.
    parent = tk.Tk()
    parent.title("Produkt bild")

    # Hämtar bilden från samma mapp
    image = PhotoImage(file="Ketchup.png")

    # Bild titel
    image_label = tk.Label(parent, image=image)
    image_label.pack()

    # Start the Tkinter event loop
    parent.mainloop()



# 10. Beräkna total priset för en vara
def calculate_total_price_per_product():



def program_render_ending(screen_pick):
    if screen_pick:
        messagebox.showinfo("Avslutar","Avslutar programet!")
    else:
        print(f"Avslutar program")


if __name__ == '__main__':
    main()