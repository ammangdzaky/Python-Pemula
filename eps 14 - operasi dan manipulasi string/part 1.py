# === OPERASI DAN MANIPULASI STRING


# 1. Menyambung string => dengan menggunakan +
awal = "akulah"
tengah = "ucup"
akhir = "kapal'laut"

nama_lengkap = awal + " " + tengah + " " + akhir
print(nama_lengkap)


# 2. menghitung panjang string => dengan menggunakan len (lenght)
print("\n" + "="*20 + str(2) + "\n")
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " adalah = " + str(panjang)) #spasi juga dihitung
# len harus dicasting dalam bentuk str karena menampilkan result berupa angka


# 3. Operator didalam string
print("\n" + "="*20 + str(3) + "\n")

# > mengecek apakah ada komponen tertentu didalam string => dgn menggunakan in atau not in
A = "A"
status = A in nama_lengkap
print("A di dalam " + "\"" + nama_lengkap + "\"" + " = " + str(status) + " (bernilai false karena yang ada a, bkn A 'kapital ngaruh')")
# in atau not in harus diubah ke string karena merupaka boolean
space = " "
status = space in nama_lengkap
print("\" \"/space di dalam " + "\"" + nama_lengkap + "\"" + " = " + str(status) )

A = "A"
status = A not in nama_lengkap
print("A tidak di dalam " + "\"" + nama_lengkap + "\"" + " = " + str(status))

# > mengulang string =>dengan menggunkan *
print("awkakowka"*5)
print(5*"awkakowka")

# > indexing => dengan menggunakan []
# index dimulai dari 0 (jadi dari kata dzaky' maka huruf k adalah index ke-3 )
print("index ke-0 dari " + nama_lengkap + " = " + nama_lengkap[0])
print("index ke-(-1) dari " + nama_lengkap + " = " + nama_lengkap[-1]) # tambah tanda min jika ingin dari belakang
print("index ke-(-5) dari " + nama_lengkap + " = " + nama_lengkap[-5])
print("index ke-(-5) dari " + nama_lengkap + " = " + nama_lengkap[-5])
# index[1:5] -> artinya index 1 sampai 5
print("index ke-(0:5) dari " + nama_lengkap + " = " + nama_lengkap[0:5])
print("index ke-(-10:-1) dari " + nama_lengkap + " = " + nama_lengkap[-10:-1])
# index [1:10:2] -> artinya ambil index 1 sampai 10 dengna selag 2
# contoh: akulahlala [0:9:2] = a u a l l
print("index ke-(0:10:4) dari " + nama_lengkap + " = " + nama_lengkap[0:10:4])

#yang terbesar => menggunakan max
print("yang terbesar nilainya didalam " + nama_lengkap + " = " + max(nama_lengkap))
# urutan nilai sesuai abjad tanda baca dan space biasanya nilainya lebih kecil dri abjad
# yang terkecil => menggunakan min
print("yang terkceil nilainya didalam " + nama_lengkap + " = " + min(nama_lengkap))

# > ASCII CODE => menggunkan ord (untuk mlihat yang terbesar dan terkecil)
# untuk meliha nilai dalam menentukan nilai suatu komponen didalam string
asci = ord(" ") #ini spasi
print("nilai ascii code dari spasi = " + str(asci))
# juga bisa melihat apasih komponen dalam ascii code tertentu => menggunakan chr
asci = 100
print("elemen dari ascii code 100 adalah = " + chr(asci))


# 4. Operator dalam bentuk method
contoh = "ular lari lurus melintasi pagar berduri merorok rorok jo kaju rorok"
jumlahR = contoh.count("r")
print("jumlah r di" + contoh + " = " + str(jumlahR))
