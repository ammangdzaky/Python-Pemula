# format string

#tanpa format (RIBET)
nama = "dzaky"
umur = 15
print("halo namaku " + nama + " umurku " + str(umur) + " tahun")

#dengan format (OMAAGAD)
nama = "dzaky"
umur = 15
format = f"halo namaku {nama}, umurku {umur} tahun"
print(format)

print("mulai".center(20,"="))

# string
print("string".center(20,"="))
str = "contoh"
format = f"contoh string : {str} "
print(format)

# boolean
print("boolean".center(20,"="))
bool = False
format = f"contoh boolean : {bool} "
print(format)

# angka
print("angka".center(20,"="))
angka = 2.25
format = f"contoh angka : {angka} "
print(format)

# bilangan bulat
print("bilangan bulat".center(20,"="))
bilangan_bulat = 20
format = f"contoh bilangan_bulat : {bilangan_bulat:d} " #jika bukan bilangan bulat maka akan eror
print(format)

# bilangan ordo ribuan -> akan menambahkan , setiap 3 angka
print("bilangan ordo ribuan".center(20,"="))
bilangan_ordo_ribuan = 2212
format = f"contoh bilangan ribuan : {bilangan_ordo_ribuan:,} "
print(format)
bilangan_ordo_jutaan = 2212021
format = f"contoh bilangan jutaan : {bilangan_ordo_jutaan:,} "
print(format)

# bulatkan angka desimal
print("bulatkan angka desimal".center(30,"="))
bulatkan_angka_desimal = 2.25023232
format = f"contoh bulatkan_angka_desimal : {angka:.2f} " # -> artinya hanya dua angka dibelakang float(koma)
print(format)

# menampilkan tanda plus dan min (pake :+)
print("min dan plus".center(20,"="))
plus = 2
mines = -2.45
format = f"contoh angka : {plus:+}\n contoh mines : {mines:+} "
print(format)

# persen
print("persen".center(20,"="))
persen = 0.255555
format = f"contoh persen : {persen:%} "
print(format)
persen = 0.255555
format = f"contoh persen : {persen:.0%} " # -> artinya buat 0 angka dibelakang koma(,)
print(format)

#operasi aritmatika didalam format
print("operasi aritmatika".center(30,"="))
barang = 5000
jumlah = 5
total = f"harga total adalah : {barang*jumlah:,}Rp "
print(total)

# format angka lain
print("format angka lain".center(30,"="))
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)