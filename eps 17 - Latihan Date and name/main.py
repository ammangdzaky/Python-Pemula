# date and time

import datetime as dt

print( "\n" + "="*35 + "\n")

print("""Selamat datang di program sederhana ini.
Ingin mengetahui hari kelahiranmu dan seberapa lama kau telah hidup?
""")
print(input("Jika ingin silahkan etik ya : "))

# begin
print("Silahkan masukkan tanggal lahir anda")
tanggal = int(input("tanggal :"))
bulan = int(input("bulan : "))
tahun = int(input("tahun : "))

lahir = dt.date(tahun,bulan,tanggal)
print(f"""Tanggal lahir anda adalah : {lahir}
Anda lahir pada hari : {lahir:%A} 
""")

#umur
sekarang = dt.date.today()
umur = sekarang - lahir
umur_tahun = umur.days // 365
umur_bulan = umur_tahun % 12
umur_hari = umur_bulan % 30
print(f"umur kamu sekarang adalah : {umur_tahun} tahun {umur_bulan} bulan {umur_hari} hari")
print("-"*10)
hari = umur.days
bulan = hari // 12
tahun = hari // 360
print(f"""Kamu telah hidup selama
{hari} hari
{bulan} bulan
{tahun} tahun
""")