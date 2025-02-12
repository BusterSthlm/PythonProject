with open('frukt.txt','r',encoding='utf-8') as fil:
    for filrad in fil:
        print(filrad.strip())

with open('frukt.txt', 'r', encoding='utf-8') as fil:
    for filrad in fil:
        print(filrad.strip(), end=' ')

#alla här läser i från denna text fill