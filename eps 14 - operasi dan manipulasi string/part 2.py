# OPERATOR-OPERATOR DALAM BENTUK METHODS


### merubah semua case/huruf pada string

# merubah ke upper case -> x.upper()
print("uppercase")
contoh = "hello world"
print("sebelum = " + contoh)
uppercase = contoh.upper()
print ("setelah = " + uppercase)

# merubah ke lower case -> x.lower()
print("lowercase")
contoh = "HEllo woRLD"
print("sebelum = " + contoh)
lowercase = contoh.lower()
print ("setelah = " + lowercase)

print("="*15)


### mengecek sesuatu menggunakan is

# hasil pengecekan adalah bbolean, casting ke str

# isupper() -> mengecek apakah semua huruf besar
contoh = "hello world"
iis = contoh.isupper()
print("setelah " + contoh + " di cek dengan isupper, hasilnya = " + str(iis))

# islower() -> mengecek apakah semua huruf kecil
contoh = "hello world"
iis = contoh.islower()
print("setelah " + contoh + " di cek dengan islower, hasilnya = " + str(iis))

# istittle() -> mengecek apakah semua kata huruf pertamnya adalah kapital
contoh = "Hello World"
iis = contoh.istitle()
print("setelah " + contoh + " di cek dengan istittle, hasilnya = " + str(iis))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

print("="*20)


### mengecek kata pertama dan terakhir dari suatu kumpulan kata menggunakan startswith() dan endswith()

# startswith()
contoh = "aku adalah atomic"
start = "aku"
cek = contoh.startswith(start)
print("apakah huruf pertama dari " + "|" + contoh + "| " + "adalah " + start + " ,jawabannya :" + str(cek))

# endswith()
contoh = "aku adalah atomic"
end = "atomic"
cek = contoh.endswith(end)
print("apakah huruf pertama dari " + "|" + contoh + "| " + "adalah " + end + " ,jawabannya :" + str(cek))

print("="*20)

### gabung dan pisah menggunakan join() dan split()

# join()
pisah = ["aku','sayang','kamu"]
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

# split()
gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

### alokasi karakter -> rjust(), ljust(), center()

#rjust() -> rata kanan
contoh = "kanan".rjust(20) # -> rata kanan dengan 20 karakter
print("|" + contoh + "|")

#ljust() -> rata kiri
contoh = "kiri".ljust(20) # -> rata kiri dengan 20 karakter
print("|" + contoh + "|")

#center() -> rata tengah
contoh = "tengah".center(20) # -> rata tengah dengan 20 karakter
print("|" + contoh + "|")

contoh = "tengah".center(20,"=") # -> agar rata tengah dengan elemen, bukan spasi
print("|" + contoh + "|")


