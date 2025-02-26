class Person:
    def __init__(self, namn,age,gender):
        self.__namn = namn
        self.__age = age
        self.__gender = gender

    def get_namn(self):
        return self.__namn

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_namn(self, namn):
        self.__namn = namn

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def __str__(self):
        return f'Personens Data:\nNamn: {self.__namn}\nÅlder: {self.__age}\nKön: {self.__gender}'

    def skriva_ut_hej(self):
        return f'Hej {self.__namn}!'
