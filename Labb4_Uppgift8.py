with open('numbers.txt','r',encoding='utf-8') as fil:
    total_Sum=0
    rad=0
    for fil_number in fil:
        rad+=1
        total_Sum+=int(fil_number)
    print(f"totala summan: {total_Sum}\nså här många rader är sparade: {rad}")