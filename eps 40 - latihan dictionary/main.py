## BISMILLAH

import os
import random
import string


template = {
    "nama" : "nama",
    "agama" : "agama",
    "fakultas" : "fakultas",
    "prodi" : "prodi",
    "hobi" : "hobi"
}

data = {}

while True:
    os.system("cls")
    print("SELAMAT DATANG".center(30,"="))
    print("DATA MAHASISWA".center(30,"="))
    print("-"*30)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa["nama"] = input("Masukkan nama : ")
    mahasiswa["agama"] = input("Masukkan agama : ")
    mahasiswa["fakultas"] = input("Masukkan fakultas : ")
    mahasiswa["prodi"] = input("Masukkan prodi : ")
    mahasiswa["hobi"] = input("Masukkan hobi : ")

    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(3)))
    data.update({KEY : mahasiswa})

    print(f"\n{"KEY":<5} {"NAMA":<13} {"AGAMA":<10} {"FAKULTAS":<13} {"PRODI":<20} {"HOBI":<13}")
    print("-"*70)

    for mahasiswa in data:

        KEY = mahasiswa

        NAMA = data[KEY]["nama"]
        AGAMA = data[KEY]["agama"]
        FAKULTAS = data[KEY]["fakultas"]
        PRODI = data[KEY]["prodi"]
        HOBI = data[KEY]["hobi"]

        print(f"{KEY:<5} {NAMA:<13} {AGAMA:<10} {FAKULTAS:<13} {PRODI:<20} {HOBI:<13}")

    stop = input("\nKetik end untuk berhenti : ")
    if stop == "end":
        break

print(f"\nPROGRAM SELESAI")


