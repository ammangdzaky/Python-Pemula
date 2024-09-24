##### IMPORT

#### Fungsi IMPORT yaitu mengambil program dari file external .py

### kegunaan


# 1. Untuk menyambung program dari external
import coba_print



# 2. Mengambil data/variable (menggunakan namespace)
import coba_variable
# print(nama) -> tidak bisa langsung begini
print(coba_variable.nama)
print(coba_variable.umur)


# 3. Import fungsi
import coba_mtk

print(coba_mtk.tambah(0,1))
print(coba_mtk.kurang(2,1))
print(coba_mtk.kali(1,1))
print(coba_mtk.bagi(1,1))
