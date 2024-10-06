import os
os.system('cls')
os.chdir("C:/Users/Dzaky/Documents/Python Pemula/eps 62 - try and except")

### try except digunakan untuk mengakali eror agar program tidak berhenti saat terjadi eror

# eror = 2/0
# print(eror) -> ini akan menghasilkan eror karna tidak bisa membagi dengan 0


# contoh 1
# pembagian
def contoh_1(a=1,b=1):
    while True:
        try:
            a = int(input("Angka yang akan dibagi: "))
            b = int(input("Angka pembagi: "))
            hasil = a / b
            print(f"Hasil: {hasil}")
        except ZeroDivisionError:
            print("Error: Tidak bisa dibagi dengan 0.")
        except ValueError:
            print("Error: Masukkan hanya bilangan bulat!")
            continue
        
        # Meminta input untuk berhenti atau lanjut
        stop = input("Berhenti (y/n)? : ").lower()
        if stop == "y":
            break
        elif stop == "n":
            continue
        else:
            print("Input tidak valid, program akan dilanjutkan.")

# contoh 2
# membaca file, jika file belum ada maka buatkan
def baca():
    try:
        with open("document.txt","r") as f:
            print(f.read())
    # jika file untuk dibaca belum ada maka akan eror FileNotFoundError
    # kode dibawah mode write/"w", maka akan membuat file baru
    except FileNotFoundError:
        with open("document.txt","w",encoding="utf-8") as f:
            f.write("INI ADALAH DOKUMEN")
        

# panggil fungsi disini
baca()


    
        