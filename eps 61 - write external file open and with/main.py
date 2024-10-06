import os
os.system("cls")
print(os.getcwd()) # untuk cek difolder mana kita sekarang
os.chdir("C:/Users/Dzaky/Documents/Python Pemula/eps 61 - write external file open and with") # untuk ganti folder tempat kita bekerja
print(os.getcwd())

'''
1. Mode 'w' (Write)
- Tujuan: Membuka file untuk menulis.
- Jika file tidak ada: File baru akan dibuat.
- Jika file sudah ada: Isi file akan dihapus (di-overwrite) dan diganti dengan konten baru yang ditulis.
- Tidak bisa membaca: Mode 'w' hanya untuk menulis, tidak bisa membaca file.

2. Mode 'a' (Append)
- Tujuan: Membuka file untuk menulis, tetapi menambahkan (append) ke bagian akhir file.
- Jika file tidak ada: File baru akan dibuat.
- Jika file sudah ada: Konten baru akan ditambahkan di akhir file tanpa menghapus isi file sebelumnya.
- Tidak bisa membaca: Mode 'a' hanya untuk menulis, tidak bisa membaca file.

3. Mode 'r+' (Read and Write)
- Tujuan: Membuka file untuk membaca dan menulis.
- Jika file tidak ada: Akan muncul error FileNotFoundError, karena mode ini membutuhkan file yang sudah ada.
- Jika file sudah ada: Kamu bisa membaca isi file dan menulis (mengganti atau menambah) konten di file tersebut tanpa menghapus keseluruhan isi file. Penulisan dimulai dari posisi kursor saat itu.
- Hati-hati dengan Overwrite: Menulis di posisi kursor bisa menimpa sebagian konten yang sudah ada, tergantung di mana kamu mulai menulis.
'''


# 1. Mode write (w)

with open("write.txt", "w", encoding="utf-8") as f:
    f.write("aku akan ditimpa")

with open("write.txt", "w", encoding="utf-8") as f:
    f.write("aku telah ditimpa")


# 2. Mode append (a)

with open("append.txt","w", encoding="utf-8") as f:
    f.write("aku tidak akan ditimpa")

with open("append.txt","a", encoding="utf-8") as f:
    f.write("aku baris pertama\n")

with open("append.txt","a", encoding="utf-8") as f:
    f.write("aku baris kedua\n")

with open("append.txt","a", encoding="utf-8") as f:
    f.write("aku baris ketiga\n")


# 3. Mode r+

with open("r+.txt","w", encoding="utf-8") as f: 
    f.write("baku akan ditimpa\n")

with open("r+.txt","r+", encoding="utf-8") as f: # -> mode r+ bisa write dan read
    f.write("baris ke 1\n")
    f.write("baris ke 2\n")
    f.write("baris ke 3\n")

with open("r+.txt","r+", encoding="utf-8") as f: 
    baca = f.read()
    print(baca)
    
with open("r+.txt","r+", encoding="utf-8") as f:
    f.write("omagad") # menimpa isi text sesuai dengan panjang data / len