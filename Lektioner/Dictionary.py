# Lektion dictionary
#Lession
# Varje nyckel ska vara unik och oföränderlig.
from traceback import extract_tb
# Key = k , Värde = v




person = {
    'namn':'Alice', # sträng, tal , tuple.
}

#Get(Finns denna nyckel?), Keys(hämtar med lista med nycklar), values(lista med värden), items(retunerar value: pair), pop( tar bort och retunerar värde), Update(uppdaterar befintlig i slutet)

print(person['namn'])
print(person.get('land', 'Ej angivet')) # Fångar upp om det inte finns.

#lägg till ny nyckel
person['yrke'] = 'Lärare'
#updatera
person['ålder'] = 26

#uppdatera dictionary med en dictionary
extra_info{'hobby':'musik'}
person.update(extra_info)

#ta bort
del person['nyckeln'] # tar bort nyckekl- värde par
#Pop
ålder = person.pop('ålder')
print(ålder) #för att visa det man har tagit bort, ålder på personen var 26...

#forloop
# Items() hämtar både key och values.
for nyckel in person.keys(): #default är att hämta keys
    print(nyckel)

#Uppdatera
Extra_info ={'hobby':'Pussel', 'husdjur':['katt 1', 'Katt 2 ', 'Katt 3']}
