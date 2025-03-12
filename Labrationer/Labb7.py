import Labb6_Class as shoping_item
import tkinter as tk
from tkinter import ttk
import json


def main():
    userList = readUserItems()
    root = tk.Tk()
    root.geometry("400x440")
    wrightUserItemlist(userList)
    get_menu_text(root)
    button_maker(root)

    root.mainloop()



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
    comandPromts=[]
    for i in range(1,12):
        tk.Button(root, text=str(i),width=5,height=1,borderwidth=1, relief="solid",command=comandPromts[i-1]).grid(row=i, column=5, columnspan=1,rowspan=1,pady=7,padx=40)









#Read and wright to JSON file and auto generate the list again to see all items corect
#lägg till Items i en array och en auto genererande ID lista
def AddItemToDictanaryWithNameID(Value):
    dictanary={}
    count=1
    #print(Value)
    for items in Value:
        #print(items)
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
    #print(items)
    for listValue in items.values():
        #print(listValue)
        #print(listKey)
        #print(listValue)
        Item_list=shoping_item.Shopping_item(listValue[0],listValue[1],listValue[2])
        #print(Item_list)
        userList.append(Item_list)
        #print(Item_list)
    return userList

#läss och skriva över spar filen
def wrightUserItemlist(item_list):
    shopList=AddItemToDictanaryWithNameID(item_list)
    #print(shopList)
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