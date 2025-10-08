# Reduce Function

faktoriyel = 1

for i in range(1,6):
    faktoriyel *= i
    
print(faktoriyel)


from functools import reduce

print(reduce(lambda x,y : x*y , range(1,6)))