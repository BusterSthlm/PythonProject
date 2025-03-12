class IceCream:
    def __init__(self, id_ic, name, price):
        # Privata attribut
        self.__id_ic = id_ic
        self.__name = name
        self.__price = price

    # Setters
    def set_id(self, id_ic):
        self.__id_ic = id_ic

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    # Getters
    def get_id(self):
        return self.__id_ic

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # String representation av objekt av klassen
    def __str__(self):
        return f"ID: {self.__id_ic}, Namn: {self.__name}, Pris: {self.__price}"


# Omvandlar objekt till dictionary (för att sedan kunna spara till JSON)
def to_dic(self):
    return {'id_ic': self.get_id(), 'name': self.get_name(), 'pris': self.get_price()} #skapr upp struktur för dictionary