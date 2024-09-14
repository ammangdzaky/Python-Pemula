# ###### LATIHAN FUNGS

import os

# def user():
#     '''fungsi input user'''
#     panjang = int(input("Masukkan Panjang : "))
#     lebar = int(input("Masukkan Lebar : "))

#     return panjang,lebar

# def luas(panjang,lebar):
#     '''fungsi luas'''
#     return panjang * lebar

# def keliling(panjang,lebar):
#     '''fungsi keliling'''
#     return 2*(panjang + lebar)

# def hasil(pilihan, nilai):
#     print(f"hasil perhitungan {pilihan} = {nilai}")

# while True:

#     os.system("cls")

#     PANJANG,LEBAR = user()

#     pilih = input("pilih hitung 'luas' atau 'keliling' : ")

#     if pilih == "luas":
#         LUAS = luas(PANJANG,LEBAR)
#         hasil("luas",LUAS)

#     elif pilih == "keliling":
#         KELILILNG = keliling(PANJANG,LUAS)
#         hasil("keliling",KELILILNG)

#     lanjut = input("ketik 'capek' jika ingin berhenti : ")

#     if lanjut == "capek":
#         break

# print(f"{"SELESAI":^30}")

def gaya():
    os.system("cls")
    print(f"{"SELAMAT DATANG":^40}")
    print(f"{"LUAS DAN KELILING SEGI EMPAT":^40}")
    print(f"="*40)
    

def user():
    panjang = int(input("masukkan panjang : "))
    lebar = int(input("masukkkan lebar : "))
    return panjang, lebar

def luas(panjang, lebar):
    luas = panjang * lebar
    return luas

def keliling(panjang, lebar):
    keliling = 2*(panjang + lebar) 
    return keliling

def hasil(jenis, akhir):
    print(f"perhitungan {jenis} = {akhir}")

def opsi():

    PANJANG,LEBAR = user()

    pilih = input(f"hitung 'luas', 'keliling', atau 'keduanya' : ")

    if pilih == "luas":
        LUAS = luas(PANJANG, LEBAR)
        hasil("luas", LUAS)
    elif pilih == "keliling":
        KELILING = keliling(PANJANG, LEBAR)
        hasil("keliling", KELILING)
    elif pilih == "keduanya":
        LUAS = luas(PANJANG, LEBAR)
        KELILING = keliling(PANJANG, LEBAR)
        hasil("luas", LUAS)
        hasil("keliling", KELILING)
    else:
        print(f"MASUKKAN OPSI YANG VALID!!!!!!!")


while True:

    gaya()

    opsi()

    stop = input("\nketik 'capek' jika anda ingin berhenti : ")
    if stop == "capek":
        break


print(f"{"SELESAI":^40}")
        
    





