# pass and continue


# Pass -> berfungsi sebagai dummy, tidak akan dieksekusi
print("pass".center(20,"="))

angka = 0
print(f"angka awal : {angka}")

print(f"setelah while")
while angka < 5:

    angka += 1

    if angka == 3:
        pass # Ini tidak akan dieksekusi sama sekali

    print(f"angka sekarang adalah : {angka}")
    

# Continue -> intinya apapun yang ada dibawah contunue akan diskip (jelasnya liat ilustrasi di gambar pada file ini)
print("continue".center(20,"="))

angka = 0
print(f"angka awal : {angka}")

print(f"setelah while")
while angka < 5:

    angka += 1

    print(f"angka sekarang adalah : {angka}") #aksi 1

    if angka == 3:
        continue #ketika bertemu 3, maka akan langsung ngeloop ke atas (aksi 1) dan menskip dibawahnya (aksi 2)

    print("halo") #aksi 2
