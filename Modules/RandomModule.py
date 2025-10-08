# Random Module Nedir ?
# Random Module Nasıl Kullanılır ?
# Random Module Örnekleri
# Random Module Fonksiyonları
# Random Module ile Neler Yapılabilir ?

import random
from random import *

sayi = random()
sayi

print("{0:.2f}".format(sayi))

sayi = uniform(5, 10)
sayi
print("{0:.2f}".format(sayi))

zar = randrange(1, 7)
zar

sayi = randrange(-100,50)
sayi

sayi = randrange(0,50,5)
sayi

zar = randint(1,7)
zar

isimler = ["Ali", "Veli", "Ayşe", "Fatma"]
print(sample(isimler,3))

isimler = ["Ali", "Veli", "Ayşe", "Fatma"]
print(choice(isimler))
