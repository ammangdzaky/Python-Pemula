# Untuk menggunakan sebuah package, install terlebih dahulu di pip menggunakan terminal
# pip install (nama package)

import numpy as np

# NUMPY berguna untuk matriks


# Perbedaan matriks dan list

list = [1,2,3,4]
print(f"\n\nlist = {list}")
matriks = np.array([1,2,3,4])
print(f"matriks = {matriks}")

# print(list**2)  -> tidak bisa bakalan eror
print(f"matriks^2 = {matriks**2}")
print(f"matriks*2 = {matriks*2}\n\n")


# matriks dengan tinggi dan panjang
# np.array([(baris 1),(baris 2),(baris strusnya)])

matriks_3x3 = np.array([(3,3,3),(3,3,3),(3,3,3)])
print(f"matriks 3x3:\n{matriks_3x3}\n\n")


# zeros = matriks yang hanya berisi nol
# np.zeros((baris,kolom))
zeros = np.zeros((3,2))
print(f"zeros:\n{zeros}\n\n")


# ones = matriks yang hanya berisi 1
# np.ones((baris,kolom))
ones = np.ones((3,3))
print(f"ones:\n{ones}\n\n")


# operasi matriks 
# misal penjumlahan

total = matriks_3x3 + (matriks_3x3**2) + (matriks_3x3*100) + ones
print(f"TOTAL:\n{total}\n\n")