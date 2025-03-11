import burk as b

burk_obj1 = b.Burk('fanta', 30, 20)
burk_obj2 = b.Burk('sprite',10,19)
burk_obj3 = b.Burk('vatten', 200, 9)

#burk_lista = [burk_obj1, burk_obj2, burk_obj3]

burk_dict ={ # inga index som i en lista
    'id1': burk_obj1,
    'id2': burk_obj2,
    'id3': burk_obj3,

}

for v in burk_dict.values():
    print(v)

for v_obj in burk_dict.values(): #hämtar Burknamn från burk.py
    print(v_obj.get_namn())

#skapa nytt obj
burk_obj = b.Burk('cola',30,15)
#Append i dictionary
burk_dict['id4'] = burk_obj

"""
for v in burk_dict.values():
    print(v)

"""

#söka via namn
namn_drycke = input('Fyll i namnet på drcken du vill ändra antal för: ')
nytt_antal = int(input('Fyll i nytt antalet'))

#hitta sprite och lägg till nytt antal
for v_obj in burk_dict.values():
    if namn_drycke == v_obj.get_namn():
        v_obj.set_antal_burkar(nytt_antal)
        print(v_obj)
