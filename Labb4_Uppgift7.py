import random
with open('numbers.txt','w',encoding='utf-8') as number_file:
    for Save_rounds in range(int(input("skriv in hur många rader du vill att datorn ska spara av random sifror: "))):
       number_file.write(str(random.randint(1, 500)) + '\n')