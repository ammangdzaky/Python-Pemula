import os
os.system("cls")

####### Global Variable

nama = "Atomic" # -> variable global

#akses di fungsi
def halo():
    print(f"halo {nama}")
halo()

#akses di if
if True:
    print(f"halo {nama}")

#akses di loop
for i in range(5):
    print(f"i ke {i} -> halo {nama}")
print("\n\n")


####### Local Variable

def local():
    lokal = "Suki" # -> variable local hanya hidup di dalam fungsi ini
# print(lokal) -> tidak bisa dilakukan / tidak bisa mengakses lokal di luar


#################### PENGGUNAAN


# 1. akses variable

def apalah():
    print(f"oi {nama}")

nama = "MAS RUDI" # -> boleh dibawah asalkan sebelum memanggil fungsinya
apalah()


# 2. mengubah nilai variable global

name = "Farhan Kebab"
alamat = "Ngawi Utara"

def ubah():
    global name # -> untuk mendapatkan akses merubah variable name
    global alamat
    name = "Rehan Wangsaff"
    alamat = "Ngawi Tenggara"

print(f"name sebelum = {name}")
print(f"alamat sebelum = {alamat}")
ubah()
print(f"name setelah = {name}")
print(f"alamat setelah = {alamat}")


## contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)
#### artinya variable di dalam if dan loop masih variable global, yang lokal hanya di dalam fungsi 