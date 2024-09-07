# ELIF statement

print("\n"+"begin".center(30,"-") + "\n")

print("Perbandingan nilai sederhana\nmasukkan 5 angka untuk dinilai yang mana yang lebih besar")

a = int(input("masukkan angka pertama : "))
b = int(input("masukkan angka kedua   : "))
c = int(input("masukkan angka ketiga  : "))

maxi = ()

if a > b and a > c:
    maxi = a
elif b > a and b > c:
    maxi = b
elif c > a and c > b:
    maxi = c

print(f"yang paling besar adalah angka : {maxi}")