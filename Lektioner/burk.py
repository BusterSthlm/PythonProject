import class_burk as burk

burk_obj1 = burk.Burk('fanta', 10, 15)
burk_obj2 = burk.Burk('cola', 20, 20)
burk_obj3 = burk.Burk('sprite', 3, 17)

#burk_obj_lista = [burk_obj1, burk_obj2, burk_obj3]

burk_dict={
    'id1':burk_obj1,
    'id2':burk_obj2,
    'id3':burk_obj3
    }

count=0
for value in burk_dict.values():
    print(f"{20*"-"}\n"+str(value))
    count+=1
    if count == len(burk_dict):
        print(f"{20*"-"}\n")

antal=int(input("hur många cola vill du ha? "))
price=int(input("hur mycket kostar 1 cola? "))

total_price=antal*price

burk_obj= burk.Burk('cola',antal,total_price)

burk_dict["id4"]=burk_obj


count=0
for value in burk_dict.values():
    print(f"{20*"-"}\n"+str(value))
    count+=1
    if count == len(burk_dict):
        print(f"{20*"-"}\n")


burk_name=input("Vad för items vill du lägga till?\n")
burk_count=int(input(f"hur många av {burk_name} vill du ha?\n"))
burk_onePrice=int(input(f"Vad kostar 1 av {burk_name}?\n"))
burk_price=burk_count*burk_onePrice
burk_obj4=burk.Burk(burk_name,burk_count,burk_price)
burk_dict["id5"]=burk_obj4
count=0
for value in burk_dict.values():
    print(f"{20*"-"}\n"+str(value))
    count+=1
    if count == len(burk_dict):
        print(f"{20*"-"}\n")


find_burk=input("Vilket item vill du ändra antalet på?")
new_count=int(input(f"hur många vill du ha av {find_burk} i stället?"))
for value_obj in burk_dict.values():
    if find_burk == value_obj.get_namn():
        value_obj.set_antal_burkar(new_count)
        value_obj.set_pris(new_count*value_obj.get_pris())

count=0
for value in burk_dict.values():
    print(f"{20*"-"}\n"+str(value))
    count+=1
    if count == len(burk_dict):
        print(f"{20*"-"}\n")