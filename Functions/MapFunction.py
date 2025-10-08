# Map Function

list1 = list(range(10))
kare = []

for i in list1:
    t = i*i
    kare.append(t)

print(kare)
print(list1)

list1 = list(range(10))
def kare(x):
    return x*x

kare_list = list(map(kare,list1))
print(kare_list)

list(map(lambda x:x*x,list1))


list1 = [1,2,3,4]
list2 = [2,3,4,5]
list3 = [3,4,5,6,7]

list(map(lambda x,y : x+y, list1,list2))

list(map(lambda x,y,z : x*y*z , list1,list2,list3))