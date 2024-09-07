# break -> akan membuat looping loncat keakhir (berhenti)

#Normal
print("\n"+"normal".center(20,"="))

angka = 0

while angka < 5:

    angka += 1
    print(f"angka sekarang adalah : {angka}")

#Contoh 1
print("\n"+"contoh 1".center(20,"="))

angka = 0

while angka < 5:

    angka += 1
    print(f"angka sekarang adalah : {angka}")

    if angka == 3:
        print("berakhir disini")
        break # jika sudah sampai di 3, maka looping akan berakhir

#Contoh 2
print("\n"+"contoh 2".center(20,"="))

selesai = int(input("akan berakhir pada angka = "))
angka = 0

while True:

    angka += 1
    print(f"angka sekarang adalah : {angka}")

    if angka == selesai:
        print("berakhir disini")
        break