from tkinter import messagebox,simpledialog

# FÖ 7 - Variabler
# FÖ 8 - inläsning från tangentbord
# FÖ 9 - fler beräkningsexempel
# FÖ 10 -Lånakalkylator
# FÖ 11 - Fstring formattering
# FÖ 12 - Fstring - grociery list
# FÖ 13 - if else
age = simpledialog.askinteger("Age", "how old are you?")
if(age >= 18):
    messagebox.showinfo(F"Your age {age}", F"you can vote because your are {age}")
else:
    messagebox.showinfo(F"your age{age}",F"You cant because {age} is not over 18")

messagebox.showinfo(F"Your age '{age}'", F"Outside the if statment")
# FÖ 13 - jämförelseoperator
tal1  = int(input('första talet'))
tal2  = int(input('första talet'))
    # operatorer <, >, >=, = , !=
if tal1 > tal2:
    print(tal1, 'är större än ', tal2 )
# FÖ 15 - MInsta tal ut av 3
talet_1 = int(input('Första talet:'))
talet_2 = int(input('andra talet:'))
talet_3 = int(input('tredej talet:'))
minsta_tal = talet_1
if talet_2 < minsta_tal:
    minsta_tal = talet_2
if talet_3 < minsta_tal:
    minsta_tal = talet_3
print("minsta tal  är:", minsta_tal)
# FÖ 16 - Nästlade ifsatser


# FÖ 17 - if elif else och debuggern
# FÖ 18 - Jämförelseoperatorn ==
# FÖ 19 - or operator
# FÖ 20 - And operator
# FÖ 21 - Not operatorn
# FÖ 22 - Debuggern
# FÖ 23 - Match satsen(styrstruken)
