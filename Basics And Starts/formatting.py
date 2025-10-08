# String Formatting - Formatlama

skor = 90
print('Skorunuz : {}'.format(skor))


eski_skor = 75
print('Skorunuz : {} , ve Eski Skorunuz : {}'.format(skor, eski_skor))


print('Skorunuz : {0} , ve Eski Skorunuz : {1}'.format(skor, eski_skor))


son_skor = 50

print('Yeni Skorunuz : {1} , eski skorunuz : {0} , ve son skorunuz : {2}'.format(eski_skor, skor, son_skor))    

# Yeni Metod Formatlama

isim = "Volkan"

print(f'Merhaba {isim}')

cevap = 42

print(f'Cevabiniz : {cevap}')

pi = 22 / 7

print(f'Pi sayisi : {pi:.2f}')

# Farkli bir gosterim sekli

print(f'Cevap : {cevap:08d}')  # 8 karakterlik yer ayirir ve bosluklari 0 ile doldurur