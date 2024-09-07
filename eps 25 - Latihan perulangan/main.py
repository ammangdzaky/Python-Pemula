# Latihan perulangan loop and while

## Loop
print("\n" + "loop".center(20,"="))

tinggi = 10
panjang = 1

for i in range(tinggi):

    print("+"*panjang)
    panjang += 1


## while
print("\n" + "loop".center(20,"="))

#segitiga siku siku
print("\n"+"1. segitiga siku siku")

tinggi = 10
panjang = 1

while True:
    
    print("+"*panjang)
    panjang += 1

    if panjang > tinggi:
        break

#segitiga siku siku tapi hanya ganjil
print("\n"+"2. segitiga siku siku tapi hanya ganjil")

tinggi = 20
panjang = 1

while True:

    print("+"*panjang)
    panjang += 2

    if panjang > tinggi:
        break
 
#segitiga sama kaki tapi hanya ganjil
print("\n"+"3. segitiga siku siku tapi hanya ganjil")

tinggi = 20
panjang = 1
spasi = int(tinggi/2)

while True:

    print(" "*spasi + "+"*panjang)
    panjang += 2
    spasi -= 1

    if panjang > tinggi:
        break

#ketupat
print("\n"+"4. ketupat")

tinggi = 20
panjang = 1
spasi = int(tinggi/2)

while True:

    print(" "*spasi + "+"*panjang)
    panjang += 2
    spasi -= 1

    if panjang > tinggi:
        break


panjang = tinggi if tinggi % 2 != 0 else tinggi - 1
spasi = 0
while True:

    print(" "*spasi+'+'*panjang)
    panjang -= 2
    spasi += 1
    if spasi > tinggi/2:
        break
    

    if panjang < 0:
        break

    
#ketupat
print("\n"+"4. ketupat input")

print("perhatian!!\njika input genap maka tinggi = tinggi\ntapi jika input ganjil maka tinggi = tinggi + 1")
tinggi = int(input("masukkan tinggi ketupat : "))
panjang = 1
spasi = int(tinggi/2)

while True:

    print(" "*spasi + "+"*panjang)
    panjang += 2
    spasi -= 1

    if panjang > tinggi:
        break


panjang = tinggi if tinggi % 2 != 0 else tinggi - 1
spasi = 0
while True:

    print(" "*spasi+'+'*panjang)
    panjang -= 2
    spasi += 1
    if spasi > tinggi/2:
        break
    

    if panjang < 0:
        break

if tinggi%2 == 0 :
    genap = tinggi
    print(f"Tinggi ketupat adalah = {genap}")
else :
    ganjil = tinggi + 1
    print(f"Tinggi ketupat adalah = {ganjil}")