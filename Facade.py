class Coffee(object):
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def coffee_on(self): #, text
        if self._count > 0:
            self._count -=1
            print(' Кофе осталось на {} чашки.' .format(self._count), end='')

class Milk(object):
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def milk_on(self): #, text
        if self._count > 0:
            self._count -=1
            print(' Молока осталось на {} чашки.' .format(self._count), end='')

class Water(object):
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def water_on(self): #, text
        if self._count > 0:
            self._count -=1
            print(' Воды осталось на {} чашки.' .format(self._count))

class Coffee_machine(object):
    def error(self, msg):
        print(' Ошибка: %s' %msg, end='\n')

    def make_coffee(self, coffee, milk, water):
        if coffee.get_count() >= 1 and milk.get_count() >= 1 and water.get_count():
            print(" Кофе готово!")
            if coffee.get_count() > 0:
                coffee.coffee_on()
            if milk.get_count() > 0:
                milk.milk_on()
            if water.get_count() > 0:
                water.water_on()
            print('________________________________________________________________________________')
        else:
            print(" Кофе не приготовлено!")
            if coffee.get_count() <= 0:
                self.error(' Нет кофе!')
            if milk.get_count() <= 0:
                self.error(' Нет молока!')
            if water.get_count() <= 0:
                self.error(' Нет воды!')
            print('________________________________________________________________________________')

class Cup_of_coffee(object):
    def __init__(self):
        self._coffee_machine = Coffee_machine()
        self._coffee = Coffee(3)
        self._milk = Milk(3)
        self._water = Water(2)

    def get_coffee(self):
        self._coffee_machine.make_coffee(self._coffee, self._milk, self._water)

Cup = Cup_of_coffee()
Cup.get_coffee()
Cup.get_coffee()
Cup.get_coffee()
Cup.get_coffee()