

# Basit Calculator

print("""
1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
5 - Kuvvet Alma
""")

fonksiyon = int(input("Yapmak istediğiniz işlemi seçiniz : "))
sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))

if fonksiyon == 1:
    print("Sonuc : " , sayi1 + sayi2)
elif fonksiyon == 2:
    print("Sonuc : " , sayi1 - sayi2)
elif fonksiyon == 3:
    print("Sonuc : " , sayi1 * sayi2)
elif fonksiyon == 4:
    if (sayi2 == 0):
        print("Bir sayı 0'a bölünemez")
    else:
        print("Sonuc : " , sayi1 / sayi2)
elif fonksiyon == 5:
    print("Sonuc : " , sayi1 ** sayi2)
else:
    print("Geçersiz işlem seçtiniz")