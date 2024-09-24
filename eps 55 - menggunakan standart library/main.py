import datetime

sekarang = datetime.datetime.now()
print(f"sekarang = {sekarang}")
print(f"sekarang tahun = {sekarang.year}")
print(f"sekarang tanggal = {sekarang.day}")
print(f"sekarang bulan = {sekarang.month}")
print(f"sekarang jam = {sekarang.hour}")
print(f"sekarang hari = {sekarang.strftime("%A")}\n\n")



from collections import Counter # -> untuk menghitung berapa jumlah suatu data dalam list

data = [1,2,21,1,2,2,3,3,4,5,64,3,3,2,3]

berapa = Counter(data)

print(berapa)
print(f"jumlah 1 yaitu : {berapa[1]}")
print(f"jumlah 2 yaitu : {berapa[2]}")
print(f"jumlah 3 yaitu : {berapa[3]}")






# list = [1,1,1,1,1,1,11,2,1,21,2,1,2,21,,1,,221,1]



