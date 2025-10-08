# Try Catch Blocks


x = int(input("Lutfen Bir Sayi Giriniz..."))
print("Girdiginiz sayi : ", x)

x = int(input("Lutfen Bir Sayi Giriniz..."))
print("Girdiginiz sayi : ", x)


try:
    x = int(input("Lutfen Bir Sayi Giriniz..."))
    if x > 0 :
        print("Girdiginiz sayi pozitif")
    else :
        print("Girdiginiz sayi negatiftir.")
except:
    print("Lutfen bir tam sayi degeri giriniz !!!")


a = int(input("Lutfen birinci sayiyi giriniz :"))
b = int(input("Lutfen ikinci sayiyi giriniz :"))

print(a / b)    