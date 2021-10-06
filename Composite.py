from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def return_sum(self):
        pass

class Box(Item):
    def __init__(self, contents):
        self.contents = contents

    def return_sum(self):
        sum = 0
        for item in self.contents:
            sum += item.return_sum()
        return sum

class Apples(Item):
    def __init__(self, cena, ves):
        self.cena = cena
        self.ves = ves

    def return_sum(self):
        self.sum_box = self.cena * self.ves
        return self.sum_box

class Pears(Item):
    def __init__(self, cena, ves):
        self.cena = cena
        self.ves = ves

    def return_sum(self):
        self.sum_box = self.cena * self.ves
        return self.sum_box

class Pineapple(Item):
    def __init__(self, cena):
        self.cena = cena

    def return_sum(self):
        return self.cena

class Coca_Cola(Item):
    def __init__(self, cena):
        self.cena = cena

    def return_sum(self):
        return self.cena

packege_of_apples = []
packege_of_apples.append(Apples(int(input('Введите цену яблок (за кг)',)), int(input('Введите вес яблок (за кг)',))))
apples_box = Box(packege_of_apples)

packege_of_pears = []
packege_of_pears.append(Apples(int(input('Введите цену груш (за кг)',)), int(input('Введите вес груш (за кг)',))))
pears_box = Box(packege_of_pears)

big_box = []
big_box.append(apples_box)
big_box.append(pears_box)
big_box.append(Pineapple(int(input('Введите цену ананаса ',))))
big_box.append(Coca_Cola(int(input('Введите цену за Coca_Cola ',))))
money = Box(big_box)

print("Потрачено денег: " +str(money.return_sum()),'грн')