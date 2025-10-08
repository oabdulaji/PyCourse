

class Ogrenciler:
    sayac = 0
    def __init__(self,isim,soyisim,adres,notlar):
        self.isim = isim
        self.soyisim = soyisim
        self.adres = adres
        self.notlar = notlar
        
        Ogrenciler.sayac += 1
    
    def fullName(self):
        return self.isim + ' ' +  self.soyisim
    
    def AddExam(self,sinav):
        self.notlar.append(sinav)

    def display(self):
        print("Ogrenci Adi : {} \nOgrenci Soyadi {} \nOgrenci Adresi {}\nOgrenci Notlari : {}".format(self.isim , self.soyisim , self.adres , self.notlar))
        print("Toplam Ogrenci Sayisi {}".format(Ogrenciler.sayac))

    def changeAdress(self,newAddress):
        self.adres = newAddress



s1 = Ogrenciler("Volkan","Atis","Istanbul",[60])
s2 = Ogrenciler("Hakan","Atis","Istanbul",[75])
s3 = Ogrenciler("Gamze","Atis","Istanbul",[90])
s4 = Ogrenciler("Hilal","Atis","Istanbul",[70])


s2.AddExam(22)
s2.AddExam(33)
s2.AddExam(44)
s2.AddExam(55)
s2.AddExam(66)

s3.AddExam(22)
s3.AddExam(33)
s3.AddExam(44)
s3.AddExam(55)
s3.AddExam(66)

s4.AddExam(22)
s4.AddExam(33)
s4.AddExam(44)
s4.AddExam(55)
s4.AddExam(66)


s1.display()
s2.display()
s3.display()
s4.display()

toplam = 0 
for i in s1.notlar :
    toplam += i

ortalama = toplam / len(s1.notlar)  

print(s1.isim + "Ortalamasi : " , ortalama)

if ortalama > 90 :
    print("Cok iyi")
elif ortalama >= 70 and ortalama < 90 :
    print("iyi")
elif ortalama >=50 and ortalama < 70 :
    print("Fena Degil")
else:
    print("Kotu")