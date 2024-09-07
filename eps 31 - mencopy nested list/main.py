################

# Untuk mencopy nested list, kita tidak cukup hanya menggunakan .copy()



# mengambil data dari nested list

a = [1,2,3]
b = [4,5,6]

data = [a,b]
print(data)

ambil = data[1][1] # -> masuk dalam lsit ke berapa -> kemudian masuk kedalam elemen keberapa
print(f"data[1][1] dari nested list diatas yaitu = {ambil}")

# address
print("\n"+"address".center(20,"="))

copy = data.copy()
print(f"Addres dari data aseli = {hex(id(data))}")
print(f"Addres dari data duplikat = {hex(id(copy))}")

print("Tapi jika liat addres list didalam list")

print(f"Addres dari list 1 di dalam data aseli = {hex(id(data[0]))}")
print(f"Addres dari list 1 di dalam data duplikat = {hex(id(copy[0]))}")


# cara mengatasinya menggunakan fungsi deepcopy
print(f"\ncara mengatasinya menggunakan deepcopy")

from copy import deepcopy

copy = deepcopy(data)
print(f"Addres dari data aseli = {hex(id(data))}")
print(f"Addres dari data duplikat = {hex(id(copy))}")

print("Tapi jika liat addres list didalam list")

print(f"Addres dari list 1 di dalam data aseli = {hex(id(data[0]))}")
print(f"Addres dari list 1 di dalam data duplikat = {hex(id(copy[0]))}")


# Contoh
print(f"\ncontoh jika saya mengganti suatu elemen maka elemen yang lain tidak keganti".center(40))

print(f"data aseli awal : {data}")
print(f"data copy awal : {copy}")

data[0][0] = 100

print(f"data aseli akhir : {data} -> pasti berubah")
print(f"data copy akhir : {copy} -> tidak akan ikut berubah")






