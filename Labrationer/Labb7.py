import Labb6_Class as shoping_item
import Labb7_Class as gui
import tkinter as tk
import json

roBool=gui.GUI()

def main():
    #userList=get_userList()
    roBool.get_root().title("Labb7 GUI")
    gemetry(roBool.get_root(),roBool.get_bools())
    get_menu_text(roBool.get_root())
    button_maker(roBool.get_root())
    roBool.get_root().mainloop()
#menu text rendering
def get_menu_text(root):
    message=["1. Lägg till varor",
             "2. Skriv ut hela listan",
             "3. Söka namn på varan & printa ut all data om varan",
             "4. Skriva ut all information om alla varor",
             "5. Uppdatera antal och pris på valt vara",
             "6. Ta bort varan ifrån nyckel fårn dictionary",
             "7. Spara shopping listan I en JSON fil",
             "8. Tömma hela shoppinglistan på varor",
             "9. Visa bild på sökt vara",
             "10.Total kostnaden",
             "11.Avsluta programet"]
    for i in range(0, 11):
        tk.Label(root, text=message[i]).grid(row=i+1, column=1, columnspan=1, rowspan=1)

def button_maker(root):
    comandPromts=[wrightUserItemlist]
    #Lägg till ,command=comandPromts[i-1] när färdig med funktonerna
    for i in range(1,12):
        button=tk.Button(root, text=str(i),width=5)
        button.grid(row=i, column=5, columnspan=1,rowspan=1,pady=7,padx=40)
        button.configure(command=comandPromts[0])

def gemetry(root,bools):
    return root.geometry(f"{get_size_up(bools)}x440")

def get_size_up(value):
    size=""
    if value:
        size="640"
    else:
        size="380"
    return size


#Read and wright to JSON file and auto generate the list again to see all items corect
#lägg till Items i en array och en auto genererande ID lista
def get_userList():
    userList = readUserItems()
    return userList

def AddItemToDictanaryWithNameID(Value):
    dictanary={}
    count=1
    for items in Value:
        ListItem = []
        key = "Item"
        key=f"{key+str(count)}"
        count+=1
        ListItem.append(items.get_name())
        ListItem.append(items.get_count())
        ListItem.append(items.get_price())
        dictanary[str(key)]=ListItem
    return dictanary

def add_items(items):
    userList=[]
    for listValue in items.values():
        Item_list=shoping_item.Shopping_item(listValue[0],listValue[1],listValue[2])
        userList.append(Item_list)
    return userList







#läss och skriva över spar filen
def wrightUserItemlist():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    save=tk.Label(roBool.get_root(),text="Sparat shoping listan i en JSON fil")
    save.grid(row=1, column=20, columnspan=20, rowspan=1)
    item_list=get_userList()
    shopList=AddItemToDictanaryWithNameID(item_list)
    with open('shoping_list.JSON', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(shopList))

def readUserItems():
    listing=[]
    try:
        with open('shoping_list.JSON', 'r', encoding='utf-8-sig') as file:
            listing = add_items(json.load(file))
    except FileNotFoundError:
        dictanary={
            "Item1":["Mjölk",2,100],
            "Item2":["Bröd",3,80],
            "Item3":["Godis",6,60]
        }
        #print(dictanary)
        listing=add_items(dictanary)
    return listing

if __name__ == '__main__':
    main()