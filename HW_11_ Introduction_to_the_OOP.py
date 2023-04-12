# Створіть класс з описом будь-якої тварини. Додайте 1 static method
class lynx:
    def __init__(self, race: str, age: int, living_place: str):
        self.race = race
        self.age = age
        self.living_place = living_place

    @staticmethod
    def predator(x):
        return 'Lynx is a predator'


Cote = lynx('northern_lynx', 5, 'Poland')
# example below
print(Cote.race)
print(Cote.predator(lynx))


# Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod

class LG:
    def __init__(self, types: str, size: bool, country: str, name: str, email: str):
        self.types = types
        self.size = size
        self.country = country
        self.name = name
        self.email = email

    def get_info(self):
        print(f"{self.name} - {self.email}")

    @classmethod
    def get_info_class(cls, data):
        types, size, country, name, email = data
        return cls(types, size, country, name, email)
    







