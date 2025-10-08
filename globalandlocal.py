# Global ve Local Değişkenler
# Global değişkenler, fonksiyonların dışında tanımlanır ve tüm fonksiyonlar tarafından erişilebilir.
# Local değişkenler ise bir fonksiyonun içinde tanımlanır ve sadece o fon
# ksiyonun içinde erişilebilir.
# Global değişkenler genellikle büyük harflerle yazılır.
# Local değişkenler ise küçük harflerle yazılır.

# def selamlama():
#     isim = "Onur" # Local değişken
#     print(isim)

# selamlama()
# print(isim) # Hata verir, çünkü isim değişkeni local'dir.   

# isim = "Onur" # Global değişken

# def selamlama():
#     isim = "Abdulaji" # Local değişken
#     print(isim)

# selamlama()
# print(isim) # Global değişkene erişebiliriz.

# a = 7
# def sayi():
#     a = 5
#     print(a) # Local değişken

# sayi()
# print(a) # Global değişken


def fonksiyon():
    global b
    b = "Merhaba Onur"
    print(b)

fonksiyon()
print(b) # Hata verir, çünkü a değişkeni henüz tanımlanmadı.