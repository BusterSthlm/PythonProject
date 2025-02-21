#def funktion(parameter)
    #return(argument)
from traceback import print_tb
from wsgiref.util import application_uri

#List and tuples
# lista_ex[1,2,3,4,] = lista som går att redigera #mutible
# tuples(1,2,3,4,5) # tuple, går inte att ändra på efter
#hömta olika datatyper
#Mutables = able to change during execution.

list1 =[10,20,30,40,50]
print(list[0])
print(list[-1]) # tar sista nummer
print(list[1:3]) # går från 1 till (inte med) 3

#.Appent()
#.remove()
#pop() Ta bort coh retunera element, det här elementet har tagits bort"
# sort()
#reverse()

lista= [1,2,3]
lista,append(8)
print()

# lägg ett värde första
#appand hamnar sista
#insert ka jag välja plats
lista[0] = 9 #Byter ut siffran på position 0

#appende
lista.append(10)
#sort
lista.sort()
lista.appent(0, 8) # Lägg siffran mellan 0 och 8
#ta bort värdet
lista.remove(5) # ange värde du vill ta bort
# ta bort med pop på positionen. Pop retunerar det värdet som den tar bort. Får det som  retur.
lista.pop(1)
deleted_item = lista.pop(1)
print (deleted_item) # kan meddel användaren att något har tagits bort.

repeadted_list = list * 3 # upprepar 3 ggr.

# Tupils, användsningsområden: koordinater.
# föreindrar oavsiktliga förändring av data.
# mindre inne än listor,
# Kan användas som som nycklar i dictionaries
# returera flera värden än funktioner
# Ex: månad,er , vokaler/konsoanter, historisk data,
# konvertera tupil till list om jag vill ändra den.
# Skapa en ny tupil om jag vill ändra min tupil.

#tupil med 1 värde
single_element_tupil =(5,) # behöver ett' , ' tecken.

# Hämta ut på en viss positon.
print(en_tuple[0]) #position
#hämta antal värden
print(en_tuple[2:6]) #position 2.3.4.5
#coutn
print(en_tuple.count(3)) #räknar alla av ett värde, hur många gånger det företkommern
#index
print(en_tuple.index(0)) #hämtar indexet för värdet jag skickar in.

#summa lista
def summa(list):
    return sum(lista)
siffror = [1,2,3]
print(summa(siffror))
#returerar en ny lista
# Extra funktioner: map(), filter()
#googla lamda
#map() =0 applicerar specifikt saker på alla värden.
#filter = villkor som en if-sats. hämta alla jämna tal delbara på 0.

#tvådimentionell lista
matris = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

#listor till textfil
frukt_lista = ['a','b','c']
with open('frukter.text', 'w', encoding=UTF-'8') as fil:
    frukt_i = fil.read().splitline()
print(frukt_i)
# fil.write('\n'.join(glass_l))

#För att kunna jobba med deta i en listformm behöver jag använda splitlines blir
#Det som en lista. Då kan jag använda den sen med append och andra funktiona

