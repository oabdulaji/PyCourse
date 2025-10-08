# Enumarate Function

meyvalar = ["Elma","Armut","Muz","Cilek","Kiraz"]
index = 0

index_meyvalar = []

for i in meyvalar :
    index_meyvalar.append((index,i))
    index +=1

print(index_meyvalar)

enumerate(meyvalar)

list(enumerate(meyvalar))

for x,y in enumerate(meyvalar) : 
    print(x,y)

for x,y in enumerate(meyvalar) : 
    if(x % 2 == 0 ) :
        print(y)