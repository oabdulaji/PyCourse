# Filter Function

list1 = [100,8,7,11,14,-6,9,200]
cift_sayilar = list(filter(lambda x: x%2==0,list1))

print(cift_sayilar)


list2 = list(range(-20,50))
negatif_sayilar = list(filter(lambda x: x<0 , list2))
print(negatif_sayilar)


# Kesisim Kumesi
list1 = [3,2,1,11,7,9]
list2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list1,list2)))


kare = map(lambda x: x*x,range(15))
list3 = list(filter(lambda x: x > 10 and x < 150,kare))
print(list3)

def asal(x):
    if x == 1:
        print("Asal bir sayi Degildir")
    elif x == 2:
        print("Asal Bir Sayidir")
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

asal(11)
asal(4)
asal(103)

asal_sayilar = list(filter(asal , range(3,1000)))
print(asal_sayilar)