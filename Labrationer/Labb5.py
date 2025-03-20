from idlelib.debugger_r import gui_adap_oid
from tkinter import messagebox, simpledialog

groceries = ["bröd\n", "mjölk\n"]

def main():
    while True:
        match get_choice():
            case 1:
                cheack_user_list("list","List have been added")
            case 2:
                read_list()
            case 3:
                add_to_list(User_input("lägg till varor","Vad för vara vill du lägga till?"))
            case 4:
                cheack_list_items("Item listed","Alla items som finns i din lista är:",True)
            case 5:
                index_list(int(User_input("Item list",f"chose a number in your list between 0-{cheack_list_items("", "", False)-1} to see ur item in the list")), cheack_list_items("", "", False))
            case 6:
                remove_index(int(User_input("Remove item",f"chose a number in your list between 0-{cheack_list_items("", "", False)-1} to remove the item")), cheack_list_items("", "", False))
            case 7:
                remove_text(str(User_input("Remove item",f"Välj ett namn i från shoping listan att ta bort")))
            case 8:
                Save_And_Add_to_list("Saved Shoping list","You shoping list have been saved!")
            case 9: #Jack
                Add_item_to_list_specific_place()
            case 10:
                Order_list_alphabeticly()
            case 11:
                Empty_whole_list()
            case 12:
                messagebox.showinfo("Avslutar","Programet håller på att avslutar sig!")
                break
            case _:
                messagebox.showwarning("Error", "Fel input skriv in rätt input för att programet ska funka!")
                pass



#get funktions
def get_choice():
    try:
        choice = int(simpledialog.askfloat("Val",f"Skriv ett nummer du i från denna lista:\n\n{render_menu_list(menu_list())}"))
    except ValueError:
        choice=12
    except TypeError:
        choice = 12
    return choice
#user inputs
def User_input(titel,message):
    return simpledialog.askstring(titel,message)+"\n"
#menu list
def menu_list():
    menu=("1. läs in text fil & lägger till i listan :\n\n",
          "2. Skriv ut listan:\n\n",
          "3. Lägg till varor/artiklar:\n\n",
          "4. Skriv ut hur många varor du har valt:\n\n",
          "5. Ange ett index för att se varan du valt:\n\n",
          "6. Ta bort vara/artikel från listan av positionen:\n\n",
          "7. Ta bort vara/artikel från listan av namnet:\n\n",
          "8. Spara listan i en txt fil:\n\n",
          "9. Lägg till vara på en specifik plats i listan:\n\n",
          "10. Sortera listan i bokstavsordning:\n\n",
          "11. Töm hela listan på varor:\n\n",
          "12. Avsluta programet:\n")
    return menu
def render_menu_list(menu):
    messege=""
    for list in menu:
        messege+=list
    return messege


# 1.
#functions of calcalations
def cheack_user_list(titel,messgae):
    try:
        with open('user_shop_list.txt', 'r', encoding='utf-8')as file:
            for items_list in file:
                add_to_list(items_list)
            messagebox.showinfo(titel,messgae)
    except FileNotFoundError:
        messagebox.showinfo("info","file not fund")

# 2.läser groceri listan
def read_list():
    user_shop_cart_list=""
    for lists in groceries:
        user_shop_cart_list = user_shop_cart_list+lists
    if user_shop_cart_list=="":
        messagebox.showinfo("List","Shoping listan är tom")
    else:
        messagebox.showinfo("List", f"Shoping listan ser ut så här\n{user_shop_cart_list}")

# 3.Lägg till i listan
def add_to_list(list):
    groceries.append(list)

# 4. Skriv ut hela listan
def cheack_list_items(titel,message,check_item_lists):
    item_list=0
    for items in groceries:
        item_list+=1
    if check_item_lists:
        messagebox.showinfo(titel,message+" "+str(item_list))
    else:
        return item_list

# 5. Välj item nummer
def index_list(number=0,item_count=0):
    if item_count > number:
        messagebox.showinfo("Item Picked", f"You have picked the item {groceries[number]}")
    else:
        messagebox.showwarning("Varning", f"Invalid nummer välj ett nummer mellan 0-{item_count - 1}")


# 6. Ta bort item från listan
def remove_index(number=0,item_count=0):
    if item_count > number:
        messagebox.showinfo("Removed Item", f"You have removed the Item {groceries[number]}")
        groceries.remove(groceries[number])
    else:
        messagebox.showwarning("Varning", f"Invalid nummer välj ett nummer mellan 0-{item_count - 1}")


# 7 Välj en plats från listan och ta bort
def remove_text(name=""):
    notfound=True
    for item in groceries:
        if name == item:
            messagebox.showinfo("Removed Item", f"You have removed the Item {item}")
            groceries.remove(item)
            notfound=False
    if notfound:
        messagebox.showwarning("Varning", f"Invalid text välj ett namn ifrån shoping listan för att remova ett item")

#8 -
# Skriv och spara groceri listan i en txt fil.
def Save_And_Add_to_list(titel,message):
    with open('user_shop_list.txt', 'w', encoding='utf-8') as fil:
        for items in groceries:
            fil.write(items)
        messagebox.showinfo(titel,message)

# 9. Lägg tillbaka item i listan på en specifik plats.
def Add_item_to_list_specific_place():
    new_item = simpledialog.askstring("New item","Add new item to shoppinglist to second place in the list :")
    index = simpledialog.askfloat("index", f"Skriv in ett nummer mellan 1-{len(groceries)+1} vart du vill i listan: ")
    groceries.insert(int(index-1),new_item+"\n")

# 10. Sorterar a-z
def Order_list_alphabeticly():
    groceries.sort(key=str.lower)
    print(groceries)



# 11.Empty_whole_list, Tar bort alla element i listan
def Empty_whole_list():
    groceries.clear()
    print(f"Your {groceries} list have been cleared")




if __name__ == '__main__':
    main()