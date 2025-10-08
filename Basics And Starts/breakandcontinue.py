# Break Ve Continue
# Break ve continue, dongulerin akisini kontrol etmek icin kullanilir.
# Break, donguyu tamamen sonlandirirken, continue ise o anki iterasyonu atlayip
# bir sonraki iterasyona gecer.

# list1 = range(11)
# for i in list1:
#     print(i)

# for i in list1:
#     print(i)
#     if(i == 5):
#         print("i 5 oldugu icin dongu sonlandiriliyor.")
#         break  # i 5 oldugunda donguyu sonlandirir.
#     print("i 5 degil, dongu devam ediyor.")

# while True:
#     isim = input("Isminizi giriniz: ")
#     print("Girdiginiz Isim : " , isim)
#     if(isim == "Onur"):
#         print("Dogru isim girdiniz, dongu sonlandiriliyor.")
#         break  # isim Onur oldugunda donguyu sonlandirir.

# num = int(input("Bir sayi giriniz .....\n "))
# if num > 1 :
#     for i in range(2,num):
#         if(num % i) == 0:
#             print("Sayimiz bir asal sayi degildir.")
#             break
#     else:
#         print(num,"bir asal sayidir.")


list1 = range(11)
for i in list1:
    print(i)

# for i in list1:
#     if i == 5:
#         print("i 5 oldugu icin bu iterasyon atlanacak.")
#         continue  # i 5 oldugunda bu iterasyonu atlar.
#     print(i)

for i in list1:
    if i == 5 or i == 7:
        print("i iterasyon atlanacak.")
        continue  # i 5 oldugunda bu iterasyonu atlar.
    print(i)