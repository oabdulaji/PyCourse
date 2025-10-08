# OS Module

import os 

os.name

os.sep

# Calistigimiz dizinin yerini verir
os.getcwd()

# chdir => Change Directory

os.listdir(os.getcwd())

# os.listdir('C:\\USER FALAN FILAN ILE GIDERIZ ORAYA VE ORAYI GETIRIR BIZE')

for i in os.listdir(os.getcwd()):
    print(i)

for i in os.listdir(os.getcwd()):
    if i.endswith('.py'):
        print(i)



# mkdir() ve mkdirs()

os.mkdir('C:\\Users\\OnurAbdulaji\\OneDrive - Tessa Group\\Desktop\\PyCourse\\TestFolder')

os.makedirs('C:\\Users\\OnurAbdulaji\\OneDrive - Tessa Group\\Desktop\\PyCourse\\TestFolder-2\\OtherTest\\OtherTest-2')

# Rename  ( oldname = newname)

os.rename("TestFolder","OsIleDosyaEkleme")

os.remove("TestFolder-2")

os.removedirs("TestFolder-2")

os.stat("Projeler")

dosya = os.stat("Projeler")

from time import *

zaman = dosya.st_atime
print(ctime(zaman))


os.system("Projeler")

