try:
    with open('slumptal2.txt','r',encoding='utf-8') as fil:
        totalCount = 0
        for filrad in fil:
            print(filrad.strip())
            totalCount += int(filrad.strip())
        print(f"Totala summan blev: {totalCount}")
except FileNotFoundError as error:
    print("File not found!\n"+str(error))