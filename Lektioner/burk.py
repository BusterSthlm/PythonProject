class Burk:
    def __init__(self, namn, antal, pris):
        self.__namn = namn
        self.__antal_burkar = antal
        self.__pris = pris


    def set_namn(self, namn):
        self.__namn = namn

    def set_antal_burkar(self, antal_burk):
        self.__antal_burkar = antal_burk

    def set_pris(self, pris):
        self.__pris = pris

    def get_namn(self):
        return self.__namn
    def get_antal_burkar(self):
        return self.__antal_burkar

    def get_pris(self):
        return self.__pris

    def __str__(self):
        utskrift = 'Namn: ' + self.get_namn() + \
            '\nAntal burkar: ' + str(self.get_antal_burkar()) + \
            '\nPris: ' + str(self.get_pris())
        return utskrift


# kod i annan pythonfil:
import burk

burk_obj1 = burk.Burk('fanta', 10, 15)
burk_obj2 = burk.Burk('cola', 20, 20)
burk_obj3 = burk.Burk('sprite', 3, 17)

burk_obj_lista = [burk_obj1, burk_obj2, burk_obj3]