import Labb6_Class as shoping_item
import Labb7_Class as gui
import tkinter as tk
import json
import os

import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image, ImageTk


roBool=gui.GUI()
groceries=[]
def main():
    #userList=get_userList()
    roBool.get_root().title("Labb7 GUI")
    roBool.get_root().config(background="White")
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=10, padx=5)
    frame.config(background="White")
    frame.grid(row=2, column=0)
    get_menu_text(frame)
    button_maker(frame)
    readUserItems()
    display_counts()
    roBool.get_root().mainloop()

##############################menu text rendering###########################################
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
    for i in range(0, 10):
        tk.Label(root, text=message[i],width=40).grid(row=i+1, column=1,pady=6)

def button_maker(root):
    comandPromts=[add_To_Item_list,find_item_serch,check_list,Render_New_Count_And_Price,RemoveKeyItemFromShopLift,wrightUserItemlist,emptyShoppingList,showImgFromSearch,totalCostPerItem, quit]
    #Lägg till ,command=comandPromts[i-1] när färdig med funktonerna
    for i in range(1,11):
        button=tk.Button(root, text=str(i),width=5)
        button.grid(row=i, column=5,pady=13,padx=40)
        button.configure(command=comandPromts[i-1])

def gemetry(root,bools):
    return root.geometry(f"{get_size_up(bools)}x600")

def get_size_up(value):
    size=""
    if value:
        size="850"
    else:
        size="380"
    return size

############################################################################################

##############################lägg till mer items 1#########################################
def add_To_Item_list():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(),pady=40,padx=5)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    mainText =tk.Label(frame,text="Lägg till en vara")
    mainText.grid(row=1, column=20, pady=7, padx=5)
    nameText = tk.Label(frame, text="Namn:")
    nameText.grid(row=2, column=20, pady=7, padx=5)
    name = tk.Entry(frame,borderwidth=1, relief="solid")
    name.grid(row=2, column=22)
    countText = tk.Label(frame,text="Antal:")
    countText.grid(row=3, column=20,pady=7,padx=5)
    count = tk.Entry(frame,borderwidth=1, relief="solid")
    count.grid(row=3, column=22)
    priceText = tk.Label(frame,text="priset (för en produkt):")
    priceText.grid(row=4, column=20,pady=7,padx=5)
    price = tk.Entry(frame,borderwidth=1, relief="solid")
    price.grid(row=4, column=22)
    messageText = tk.Text(frame,width=30,height=3,borderwidth=1, relief="solid")
    button=tk.Button(frame,text="Lägg till I shoping listan",command=lambda :add_List([name.get(),int(count.get()),int(price.get())],messageText))
    button.grid(row=5, column=20,pady=20)
    messageText.grid(row=6, column=20)

def add_List(list,messageText):
    Item_list = shoping_item.Shopping_item(list[0], list[1], list[2])
    messageText.insert(1.0,str(f"Name: {list[0]}\nAntal: {list[1]}st\nPriset (för en produkt): {list[2]}kr\n{30*"-"}\n"))
    groceries.append(Item_list)
    display_counts()
############################################################################################
############################print out antalet 2#############################################
def get_total_count():
    counts = groceries
    return counts
#def sendResolt(awnser):
#    pick = tk.Label(roBool.get_root())
#    if awnser.get() == "M":
#        pick.config(text=f"Antal varor som finns i listan: {len(get_total_count())}")
#        pick.grid(row=12, column=7)
#    if awnser.get() == "N":
#        pick.config(text=f"                                                        ")
#        pick.grid(row=12, column=7)
#def display_counts():
#    roBool.set_bools(True)
#    gemetry(roBool.get_root(), roBool.get_bools())
#    val = tk.StringVar()
#    tk.Radiobutton(roBool.get_root(),text="on",variable=val, value="M").grid(row=1,column=10)
#    tk.Radiobutton(roBool.get_root(),text="off",variable=val, value="N").grid(row=1,column=15)
#    tk.Button(roBool.get_root(),text="Turn On/Off",command=lambda :sendResolt(val)).grid(row=3,column=13)
def display_counts():
    tk.Label(roBool.get_root(),text=f"Antal varor som finns i listan: {len(get_total_count())}").grid(row=3, column=0)

############################################################################################
############################Sök på valfri vara 3############################################
def find_item_serch():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=80,padx=40)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame, text="Sök på en vara").grid(row=3, column=23, pady=7, padx=5)
    nameText = tk.Label(frame, text="Namn:")
    nameText.grid(row=4, column=20, pady=7, padx=5)
    name = tk.Entry(frame, borderwidth=1, relief="solid")
    name.grid(row=4, column=23)
    messageText = tk.Text(frame, width=30, height=3.5, borderwidth=1, relief="solid")
    button = tk.Button(frame, text="Sök I listan",command=lambda: list_name(name,messageText))
    button.grid(row=5, column=23,pady=20)
    messageText.grid(row=6, column=23)
def list_name(name,messageText):
    items=groceries
    for item in items:
        if name.get() == item.get_name():
            messageText.insert(1.0,str(item))
############################################################################################
############################Print out all info 4############################################
def check_list():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(),pady=80,padx=70)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame, text="Alla varor").grid(row=1, column=20, pady=7, padx=5)
    user_list =groceries
    messageText = tk.Text(frame, width=30, height=16, borderwidth=1, relief="solid")
    for list in user_list:
        messageText.insert(1.0,str(list))
    messageText.grid(row=3, column=20)
############################################################################################
#########################uppdatera antal och pris 5#########################################
def Render_New_Count_And_Price():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=50, padx=40)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame, text="Byta Antal och Pris").grid(row=1, column=20, pady=7, padx=5)
    ###Name
    nameText = tk.Label(frame, text="Namn:")
    nameText.grid(row=2, column=20, pady=7, padx=5)
    Name = tk.Entry(frame, borderwidth=1, relief="solid")
    Name.grid(row=2, column=25)
    ###antal
    CountText = tk.Label(frame, text="Antal:")
    CountText.grid(row=3, column=20, pady=7, padx=5)
    Count = tk.Entry(frame, borderwidth=1, relief="solid")
    Count.grid(row=3, column=25)
    ###Pris
    PriceText = tk.Label(frame, text="Prise (för en vara):")
    PriceText.grid(row=4, column=20, pady=7, padx=5)
    Price = tk.Entry(frame, borderwidth=1, relief="solid")
    Price.grid(row=4, column=25)
    tk.Label(frame,text="Updaterad resultat").grid(row=7, column=25)
    messageText = tk.Text(frame, width=20, height=4, borderwidth=1, relief="solid")
    button = tk.Button(frame, text="Söka & Updatera",command=lambda :SearchName_ChangeCountAndPrice(Name.get(),Count,Price,messageText))
    messageText.grid(row=8, column=25)
    button.grid(row=5, column=25,pady=20)
def SearchName_ChangeCountAndPrice(Item_Name,Count,Price,messageText):
    shopingList=groceries
    for list in shopingList:
        if list.get_name() == Item_Name:
            list.set_count(int(Count.get()))
            list.set_price(int(Price.get()))
            messageText.insert(1.0,str(list))
############################################################################################
########################Ta bort Key från derectanary 6######################################
def RemoveKeyItemFromShopLift():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=50, padx=40)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame,text="Ta bort Varan Ifrån Key (i dictanary)").grid(row=2,column=20)
    dictList=AddItemToDictanaryWithNameID(groceries)
    generate_keyNames(dictList,frame)
    ###ItemList
    itemText = tk.Label(frame, text="vilket item i listan vill du ta bort:")
    itemText.grid(row=3, column=20, pady=7, padx=5)
    item = tk.Entry(frame, borderwidth=1, relief="solid")
    item.grid(row=4, column=20)
    ButtonFrame=tk.Frame(frame,pady=10,padx=10)
    ButtonFrame.config(background="White")
    ButtonFrame.grid(row=5, column=20)
    if len(groceries) != 0:
        button = tk.Button(ButtonFrame, text="Ta bort Item",command=lambda: removeItemUpdate(item.get(),frame))
        button.grid(row=5, column=20, pady=20)
    else:
        NoButton = tk.Button(ButtonFrame, text="Ta bort Item")
        NoButton.grid(row=5, column=20, pady=20)
def generate_keyNames(lists,frame):
    titel = tk.Label(frame, text="All keys du kan ta bort")
    titel.grid(row=2,column=21,pady=10,padx=10)
    instruction = tk.Label(frame, text="Exempel på hur du skriver in:\nItem1")
    instruction.grid(row=3, column=21, pady=10, padx=10)
    if len(lists) > 0:
        names = tk.Label(frame, text=f"Item1-{len(lists)}")
        names.grid(row=4, column=21, pady=10, padx=10)
    else:
        names = tk.Label(frame, text=f"Du har inget I din lista!\nLägg till Items i din lista\nför att fortsätta!")
        names.grid(row=4, column=21, pady=10, padx=10)


def removeItemUpdate(list,frame):
    choice=""
    dictList = AddItemToDictanaryWithNameID(groceries)
    for keys in dictList.keys():
        if list == keys:
            choice=list
    removeItem(choice,dictList,frame)
    display_counts()

def removeItem(name,dictlist,frame):
    save=groceries
    index=0
    for keys,value in dictlist.items():
        #print(keys) Här kan man se testnings sättet man kan använda för att se om saker passerar
        #print(name)
        if name == keys:
            #print("Pass1")
            if value[0] == save[index].get_name():
                #print("Pass2")
                corectIndex=index
                groceries.pop(corectIndex)
        #print("NoPass")
        index+=1
    generate_keyNames(groceries, frame)


############################################################################################
#######################read and wrirgt till JSON file 7#####################################
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
        groceries.append(Item_list)
    return userList

#läss och skriva över spar filen
def wrightUserItemlist():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=200, padx=110)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    save=tk.Label(frame,text="Sparat shoping listan i en JSON fil")
    save.grid(row=5, column=20, columnspan=20, rowspan=1)
    item_list=groceries
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
############### Empty Shopping list ################
def emptyShoppingList():

    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())

    frame = tk.Frame(roBool.get_root(), pady=50, padx=40, background="White")
    frame.grid(row=2, column=30)

    # Labels & Buttons
    tk.Label(frame, text="Rensa listan").grid(row=1, column=20, pady=7, padx=5)
    tk.Text(frame, height=5, width=30).grid(row=4, column=0, columnspan=3)


    # Skriver ut bekräftelse
    result_label = tk.Label(frame, text="", background="White")
    result_label.grid(row=3, column=0, pady=10)
    tk.Button(frame, text="töm listan", command=lambda:empty(result_label)).grid(row=2, column=0)  # Fixed button command

def empty(resultat):
    groceries.clear()
    try:
        with open('shoping_list.JSON', 'r', encoding='utf-8-sig') as file:
            os.remove('shoping_list.JSON')
    except FileNotFoundError:
        pass
    resultat.config(text="listan har blivit tömt")




######################### SHOW IMG FROM SEARH #############
def showImgFromSearch():
#Skapar ut vyn för GUI
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=50, padx=40)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame,text="Sök och visa produkt").grid(row=1, column=20, pady=7, padx=5)
    query_item = tk.Entry(frame, borderwidth=1, relief="solid")
    query_item.grid(row=2,column=20)

    tk.Button(frame,text="sök", command=lambda: fetch_image(query_item.get(),frame)).grid(row=3, column=20, pady=7, padx=5)


def fetch_image(query,frame):

    search_url = f"https://www.google.com/search?tbm=isch&q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    image_tags = soup.find_all("img")
    img_label= tk.Label(frame)
    if len(image_tags) > 1:
        img_url = image_tags[1]["src"]  # Första bilden är oftast Googles logga, så vi tar den andra
        image_response = requests.get(img_url)
        img_data = Image.open(BytesIO(image_response.content))
        img_data = img_data.resize((300, 300))  # Ändra storlek på bilden
        img = ImageTk.PhotoImage(img_data)



        img_label.config(image=img)
        img_label.image = img
    else:
        img_label.config(text="Ingen bild hittades.")
    img_label.grid(row=1, column=20, pady=7, padx=5)





def totalCostPerItem():
    roBool.set_bools(True)
    gemetry(roBool.get_root(), roBool.get_bools())
    frame = tk.Frame(roBool.get_root(), pady=200, padx=110)
    frame.config(background="White")
    frame.grid(row=2, column=30)
    tk.Label(frame, text="Sök på en vara för att få fram totala priset").grid(row=2, column=20)
    tk.Label(frame,text="Namn:").grid(row=3, column=20)
    product_name = tk.Entry(frame, borderwidth=1, relief="solid")
    product_name.grid(row=3, column=25)
    tk.Button(frame, text="Beräkna varan",  command=lambda:calculation(product_name,frame)).grid(row=4, column=20 ) # funktionnamn, prodctu name, frame



def calculation(product_name, frame):
    # beräkning
    for name in groceries:
        if name.get_name() == product_name:
            total_price = name.get_count() * name.get_price()
            tk.Label(frame, text=f"totala priset på varan: {total_price} kr")
            result_label = tk.Label(frame, text="")
            result_label.grid(row=5, column=20)






def quit():
    exit()



############################################################################################
if __name__ == '__main__':
    main()



#### TEST IMG
