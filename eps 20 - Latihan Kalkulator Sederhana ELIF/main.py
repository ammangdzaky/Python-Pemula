# KALKULATOR SEDERHANA

print("\n" + "KALKULATOR SEDERHANA".center(40,"=") + "\n")

input("ketik ya untuk memulai : ")

print(f"Silahkan Masukkan Angka dan Operasi")

a = int(input("angka pertama     : "))
b = input(("operasi (+ - x /)     : "))
c = int(input("angka kedua       : "))

print("="*10)

if b == "+":
    print(f"{a} + {c} hasilnya = {a+c}")
elif b == "-":
    print(f"{a} - {c} hasilnya = {a-c}")
elif b == "x":
    print(f"{a} x {c} hasilnya = {a*c}")
elif b == "/":
    print(f"{a} / {c} hasilnya = {a/c}")
else:
    print("silahkan masukkan operasi yang benar (+ - x /)")
