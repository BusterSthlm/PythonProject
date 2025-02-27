# Vad är OOP
# Process > steg 1,2,3

#abstration = modellera verkligen i förenklat sätt.
# UML klass diagram för klassen Car
# Klass = en mall för att skapa objekt
# Objekt = en instans av en klass
    # Klass bil
        # Objekt = färg, röd, märke,volvo

#class
class Bil:
    pass #En tom class

#__init__:
# En konstruktur - Vilket tillstånd ska den här klassen när den skapas upp.
# Initiala värden, som bokens titel, namn på författare.

bil_obj = Bil("volvo", "XC60",2022)

class fordon:
    def __init__(self,marke, modell,ar): # parametrar #Konstruktorn
        self.marke = marke #argument , #Self pekar på sig själv.

#instansmetoder
def beskrivning_bil(self):
    return f"denna bild är en {self.marke} {self.modell}"

#Arv och klasser
#Ärver från superklassen (fordon)
class bil(fordon):
    def __init__(self):
        return

#inkapsling
#skapar privata attribut och metoder
class bank:
    #Privata attribut har två __ under sig.
    def get_marke(self):
        return
    def set_marke(self,marke):
        return

 #Polymorfiska.
#Metodöverskuggning
# Superklass = hur ett hurdjur låter
    #subclass = tar efter superklassen
class djur: #Superklass
        def göra_ljud(self):
            return

class Hund(djur): #subklass
    def göra_djur(self):
        return 'Voff'

class Katt(djur): #subklass
    def göra_ljud(self):
        return 'Mjau'

djur = djur()
print(djur.göra_ljud())
print(Hund.göra_ljud())
print(Katt.göra_ljud())

#samma metodnman skan ha olika funktionalitet i olika klasser.
#Djur



