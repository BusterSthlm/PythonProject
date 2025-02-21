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
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
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
    menu=("läs in text fil & lägger till i listan 1:\n\n",
          "skriv ut listan 2:\n\n",
          "Lägg till varor/artiklar 3:\n\n",
          "Skriv ut hur många varor du har valt 4:\n\n",
          "Ange ett index för att se varan du valt 5:\n\n",
          "Ta bort vara/artikel från listan av positionen 6:\n\n",
          "Ta bort vara/artikel från listan av namnet 7:\n\n",
          "Spara listan i en txt fil 8:\n\n",
          "Lägg till vara på en specifik plats i listan 9:\n\n",
          "Sotera listan i bokstavsordning 10:\n\n",
          "Töm hela listan på varor 11:\n\n",
          "Avsluta programet 12:\n")
    return menu
def render_menu_list(menu):
    messege=""
    for list in menu:
        messege+=list
    return messege


#functions of calcalations
def cheack_user_list(titel,messgae):
    try:
        with open('user_shop_list.txt', 'r', encoding='utf-8')as file:
            for items_list in file:
                add_to_list(items_list)
            messagebox.showinfo(titel,messgae)
    except FileNotFoundError:
        messagebox.showinfo("info","file not fund")

def add_to_list(list):
    groceries.append(list)

def cheack_list_items(titel,message,check_item_lists):
    item_list=0
    for items in groceries:
        item_list+=1
    if check_item_lists:
        messagebox.showinfo(titel,message+" "+str(item_list))
    else:
        return item_list

def index_list(number=0,item_count=0):
    if item_count > number:
        messagebox.showinfo("Item Picked", f"You have picked the item {groceries[number]}")
    else:
        messagebox.showwarning("Varning", f"Invalid nummer välj ett nummer mellan 0-{item_count - 1}")

def remove_index(number=0,item_count=0):
    if item_count > number:
        messagebox.showinfo("Removed Item", f"You have removed the Item {groceries[number]}")
        groceries.remove(groceries[number])
    else:
        messagebox.showwarning("Varning", f"Invalid nummer välj ett nummer mellan 0-{item_count - 1}")

def remove_text(name=""):
    notfound=True
    for item in groceries:
        if name == item:
            messagebox.showinfo("Removed Item", f"You have removed the Item {item}")
            groceries.remove(item)
            notfound=False
    if notfound:
        messagebox.showwarning("Varning", f"Invalid text välj ett namn ifrån shoping listan för att remova ett item")



#Read and write functions
#read groceries list
def read_list():
    user_shop_cart_list=""
    for lists in groceries:
        user_shop_cart_list = user_shop_cart_list+lists
    if user_shop_cart_list=="":
        messagebox.showinfo("List","Shoping listan är tom")
    else:
        messagebox.showinfo("List", f"Shoping listan ser ut så här\n{user_shop_cart_list}")

#write and save the groceries list in a txt file
def Save_And_Add_to_list(titel,message):
    with open('user_shop_list.txt', 'w', encoding='utf-8') as fil:
        for items in groceries:
            fil.write(items)
        messagebox.showinfo(titel,message)


if __name__ == '__main__':
    main()