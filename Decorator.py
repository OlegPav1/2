class Solder(object):
    def __init__(self, name):
        self._name = name

    def say(self):
        self.hull_protection = 0
        self.head_protection = 0
        self.leg_protection = 0
        print ('Создан персонаж - '+self._name +'. Защита корпуса - ' +str(self.hull_protection), '%, Защита головы - '+str(self.head_protection), '%, Защита ног - '+str(self.leg_protection), '%')

class militari_body_armor(object):
    def __init__(self, solder):
        self._solder = solder

    def __getattr__(self, item):
        return getattr(self._solder, item)

    def body_armor(self):
        self._solder.hull_protection += 60
        print('На '+self._solder._name, 'одет бронежилет. Защита корпуса - ' +str(self.hull_protection), '%, Защита головы - '+str(self._solder.head_protection), '%, Защита ног - '+str(self._solder.leg_protection), '%')

    def helmet(self):
        self._solder.head_protection += 50
        print('На '+self._solder._name, 'одет шлём. Защита корпуса - ' +str(self.hull_protection), '%, Защита головы - '+str(self._solder.head_protection), '%, Защита ног - '+str(self._solder.leg_protection), '%')

    def boots(self):
        self._solder.leg_protection += 45
        print('На '+self._solder._name, 'одеты ботинки. Защита корпуса - ' +str(self.hull_protection), '%, Защита головы - '+str(self._solder.head_protection), '%, Защита ног - '+str(self._solder.leg_protection), '%')


solder = Solder(input('Введите имя персонажа '))
solder_jetpack = militari_body_armor(solder)
solder_jetpack.say()
a= input('Одеть бронежилет? (+/-)')
if a == '+':
    solder_jetpack.body_armor()
b= input('Одеть шлём? (+/-)')
if b == '+':
    solder_jetpack.helmet()
c= input('Одеть ботинки? (+/-)')
if c == '+':
    solder_jetpack.boots()
