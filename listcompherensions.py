# List Compherensions nedir ?   
# List Compherensions ile nasil kullanilir ?
# List Compherensions ile nasil filtreleme yapilir ?
# List Compherensions ile nasil kosul eklenir ?

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []

# for i in list1:
#     list2.append(i)
# print(list2)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [i for i in list1]
# print(list2)


# list1 = [4,5,6,7]
# list2 = [i*i for i in list1]
# print(list2)

# kelime = "Merhaba"
# string_list = [i*3 for i in kelime]
# print(string_list)

# list1 = [(2,3) , (4,5) , (1,2)]
# list2 = [x*y for x,y in list1]
# print(list2)


# renkler = ["Kirmizi" , "Mavi" , "Yesil" , "Sari"]
# meyveler = ["Elma" , "Armut" , "Muz" , "Cilek"]
# renkli_meyveler = [(x,y)for x in renkler for y in meyveler]
# print(renkli_meyveler)


# list1 = [i*3 for i in range(1,100,5)]
# print(list1)

# list1 = [i for i in range(1,20) if i>3 and i<10]
# print(list1)

# list1 = [[1,2] , [3,4,5] , [6,7,8,9,10]]
# for i in list1:
#     print(i)

# list1 = [[1,2] , [3,4,5] , [6,7,8,9,10]]
# for i in list1:
#     for x in i:
#         print(x)

# list1 = [[1,2] , [3,4,5] , [6,7,8,9,10]]
# list2 = []
# for i in list1:
#     for x in i:
#         list2.append(x)
# print(list2)

list1 = [[1,2] , [3,4,5] , [6,7,8,9,10]]
list2 = [x*x for i in list1 for x in i]
print(list2)