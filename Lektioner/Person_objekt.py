#Övning - skapa en person

class Person:
    #konstruktor
    def __init__(self,namn_p ):
        self.namn = namn_p # publikt attribut UTAN 2 __
    # namn_p blir startvärdet, self.namn är attributen som tillhör objektet.

person_obj = Person('Kalle') # Anropar obstruktorn
print(person_obj.namn)
#objektet får vi inte ut i läsbarform __str__

def __str__(self):
    return f'Välkommen{self.namn}!'

def skriva_ut_hej(self):
    hej = f'hej{self.namn}'
    return

person_obj = Person('Kalle') # Anropar obstruktorn
print(person_obj) #kan skriva ut objektet pga __str__
print(person_obj.skriva_ut_hej())

#Privat och publikt attribut

#Get och set
def get_namn(self):
    return self.__namn

def set_namn(self, namn): # 'namn' är det nya namnet jag ska byta från kalle till KARL.
    self.__namn = namn
def __str__(self):


person_obj.getnamn()
person_obj.__namn = 'Karl'
#när en metod retunerar måste vi fånga upp det om vi ska göra något med den

# LEKTION 2


