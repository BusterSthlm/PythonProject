import class_list_Person as p


person_obj1 = p.Person('lisa',18,'female')
person_obj2 = p.Person('lasse',45,'male')
person_obj3 = p.Person('kalle',49,"anka")
person_obj4 = p.Person('kajsa',46,'anka')

person_list=[person_obj1,person_obj2,person_obj3,person_obj4]

while True:
    val = input('välj altarnativ\n1- skriv ut alla\n2- lägga till\n0- avsluta program\n')
    match val:
        case '1':
            for p_obj in person_list:
                print(p_obj)
        case '2':
            namn = input('lägg till namn: ')
            age = input('lägg till ålder: ')
            gender = input('lägg till kön: ')
            add_person_obj = p.Person(namn,age,gender)
            person_list.append(add_person_obj)
        case '0':
            print("Avslutar programet")
            break





'''
person_obj1 = p.Person('lisa',18,'female')
person_obj2 = p.Person('lasse',45,'male')
person_obj3 = p.Person('kalle',49,"anka")
person_obj4 = p.Person('kajsa',46,'anka')

person_list=[person_obj1,person_obj2,person_obj3,person_obj4]

for person in person_list:
    print(person)
'''


'''
list = ["lisa","lasse","kalle","kajsa","yoda"]
for name in list:
    person_obj = p.Person(name)
    print(person_obj)
    print(person_obj.skriva_ut_hej())
    print(person_obj.get_namn())
'''




#person_obj = p.Person('Kalle')
#print(person_obj)
#print(person_obj.get_namn())
#print(person_obj.skriva_ut_hej())
#person_obj.set_namn('Karl')
#print(person_obj)
#print(person_obj.get_namn())
#print(person_obj.skriva_ut_hej())
#print(person_obj)
#print(person_obj.skriva_ut_hej())
#print(person_obj.__namn)