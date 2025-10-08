# Return Value In Functions nedir ?
# Return Value In Functions, bir fonksiyonun çalışması sonucunda bir değer döndürmesini sağlar.
# Bu değer, fonksiyonun çağrıldığı yerde kullanılabilir veya başka işlemler için saklanabilir.
# Return ifadesi, fonksiyonun çalışmasını sonlandırır ve belirtilen değeri döndürür.


# def kare(x):
#     a = x * x

# kare(5)

# type(kare(5))  # NoneType


# def kare(x):
#     a = x * x
#     return a  # return ifadesi ile a değişkeninin değeri döndürülüyor.

# kare(5)

# print(kare(5))  # 25


# def double(sayi):
#     return sayi * 2

# double(3)  # 10


# def toplam(a,b,c):
#     x = a + b + c
#     return x

# toplam(2,3,4)  # 9


# def double(a):
#     return a * 2

# def kare(b):
#     return b * b

# def toplam(c):
#     return c + 3

# print(toplam(kare(double(2))))


def cember(yaricap):
    alan = 3.14 * yaricap ** 2
    cevre = 2 * 3.14 * yaricap
    return alan, cevre  # Fonksiyon birden fazla değer döndürebilir.

x,y =  cember(5)
print(x)  # 78.5
print(y)  # 31.400000000000002 