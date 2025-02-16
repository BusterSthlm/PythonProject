with open('numbers.txt','r',encoding='utf-8') as fil:
    total_Sum=0#variable för inne i filen
    rad=0#variable för inne i filen
    for fil_number in fil:
        rad+=1 #lägger till en rad som den har läst in
        total_Sum+=int(fil_number) #räknar ihop till en total summa
    print(f"totala summan: {total_Sum}\nså här många rader är sparade: {rad}")#srkiver ut alla svaren på skärmen