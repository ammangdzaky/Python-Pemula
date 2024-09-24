import os
os.system("cls")

######################################

# 1
import package.mtk

tambah = package.mtk.tambah(1,2,3,4,5,6,7,8,)
print(f"tambah = {tambah}")

# 2 
import package.mtk as cihuy

kurang = cihuy.kurang(100,2,2,2,2,2,2)
print(f"kurang = {kurang}")


# 3
from package import mtk

kali = mtk.kali(1,2,9)
print(f"kali = {kali}")


# 4
from package import mtk as omagad

tambah = omagad.tambah(999,22,121)
print(f"tambah = {tambah}")


# 6 
from package.list import ganjil
from package.list import genap

list = [1,2,3,4,5,5,6,76,3,22,43,44]

ganjil = ganjil(list)
genap = genap(list)
print(ganjil)
print(genap)


# 7
from package.list import prima as oooomagad

list = [1,2,3,4,5,6,7,7,8,9,0,1,2,3,22,1,344,3,4,223,4,5,3545,56,6,67,11,2111,12,0,13,0]

prima = oooomagad(list)

print(prima)

