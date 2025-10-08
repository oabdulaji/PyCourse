# IF ELIF ELSE DURUMU

# sayi = int(input("Bir sayi giriniz: "))
# if sayi > 0:
#     print("Sayi pozitif")
# else:
#     print("Sayi pozitif degil")

# sayi = int(input("Bir sayi giriniz: "))
# if sayi > 0:
#     print("Sayi pozitif")
# elif sayi == 0:
#     print("Sayi notr")
# else:
#     print("Sayi negatif")

# ulke = input("Bir ulke giriniz: ")
# if ulke == "TR":
#     print("Ulasma zamani 10 Gundur.")
# elif ulke == "GR":
#     print("Ulasma zamani 7 Gundur.")
# elif ulke == "USA":
#     print("Ulasma zamani 15 Gundur.")
# elif ulke == "FR":
#     print("Ulasma zamani 3 Gundur.")    
# elif ulke == "CH":
#     print("Ayni Gun Kargoya Verilir.")  
# else:
#     print("Ulasma zamani 1 Gundur.")


yas = int(input("Yasinizi giriniz: "))
if yas > 80:
    print("Yasiniz 80'den buyuk oldugu icin biletiniz ucretsizdir.")
elif yas < 79 and yas > 65:
    print("Yasiniz 65-79 arasinda oldugu icin biletiniz %50 indirimlidir.")
elif yas < 65 and yas > 18:
    print("Yasiniz 18-65 arasinda oldugu icin biletiniz tam fiyattir.")
else:
    print("Yasiniz 18'den kucuk oldugu icin biletiniz ucretsizdir.") 