fruk_lista=["bannan","apelsin"]

with open('frukt.txt','w',encoding='utf-8') as fil:
    fil.write('äpple\n')
    fil.write('Päron\n')
    for frukt in fruk_lista:
        fil.write(frukt+'\n')

#verskrider allt i text filen