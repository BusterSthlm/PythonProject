class Shopping_item:
    def __init__(self,name,count,price):
        self.__name = name
        self.__count = count
        self.__price = price

    #get funktion för att hämta infon som är sparad
    def get_name(self):
        return self.__name
    def get_count(self):
        return self.__count
    def get_price(self):
        return self.__price

    #set funktion ändrar vädert på de item du har valt
    def set_name(self,name):
        self.__name = name
    def set_count(self,count):
        self.__count = count
    def set_price(self,price):
        self.__price = price

    #str string variable som sickar ut slut texten
    def __str__(self):
        return f"Du valde item:\nNamn: {self.__name}\nAntal: {self.__count}st\nPriset: {self.__price}kr\n{20*"-"}\n"