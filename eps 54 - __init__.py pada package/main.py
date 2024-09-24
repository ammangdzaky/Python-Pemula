import os 
os.system("cls")

#######################################################


import package  ### -> HANYA INI IMPORT YANG DIPAKE 


tambah = package.mtk.tambah(1,2,2,2,221,1222) # PANJANG CUI
print(f"tambah = {tambah}")

kurang    = package.kurang(100,-100)        #rapi (cek __init__.py untul caranya)
kali      = package.kali(100,999)       #rapi (cek __init__.py untul caranya)
pangkat10 = package.pangkat(10)     #rapi (cek __init__.py untul caranya)
print(f"kurang = {kurang}")
print(f"kali = {kali}")
print(f"pangkat 10 = {pangkat10(999)}")


##############################

data = [1,2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

ganjil = package.listt.list.ganjil(data)
genap = package.list.genap(data)
print(ganjil)
print(genap)


prima = package.prima(data)
print(prima)