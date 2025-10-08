

class Elemanlar():
    def __init__(self,isim,yas,maas):
        self.isim = isim
        self.yas = yas
        self.maas = maas

    def display(self):
        print("Elemanin Adi : {}  Elemanin Yasi :  {} Elemanin Maasi : {}".format(self.isim , self.yas , self.maas))

eleman1 = Elemanlar("Volkan",35,2500)
eleman2 = Elemanlar("Gamze",30,2000)
eleman3 = Elemanlar("Hakan",20,3000)

eleman1.display()

# e1 = Elemanlar()
# e2 = Elemanlar()
# e3 = Elemanlar()

# e1.isim = "Onur"
# e1.yas = 35
# e1.maas = 2500

# e2.isim = "Hamza"
# e2.yas = 30
# e2.maas = 2000

# e2.isim = "Hakan"
# e2.yas = 20
# e2.maas = 3000

