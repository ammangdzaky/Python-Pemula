### DEFAULT ARGUMENT PADA FUNGSI


# def fungsi(argument = deafult argument):



print("="*20)  ## ------------> CONTOH 1


def halo(objek = "manusia"):  # "manusia" adalah default argument
    '''fungsi halo'''
    print(f"Hai {objek}")

halo("memet")
halo()


print("="*20)  ## ------------> CONTOH 2


def hai(nama , sapaan = "apa kabar?"):
    '''fungsi sapaan'''
    print(f"hai {nama}, {sapaan}")

hai("dzaky", "apa kareba?")
hai("suki") ## --> otomatis menggunakan  default pada argument sapaan karena kosong


print("="*20)  ## ------------> CONTOH 3


def kuadrat(angka , pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(kuadrat(10,10))
print(kuadrat(10))

hasil = kuadrat(angka = 11 , pangkat = 11)

print(hasil)


print("="*20)  ## ------------> CONTOH 4


def math(angka_1=2 , angka_2=2 , angka_3=2 , angka_4=2 , angka_5=2):
    hasil = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
    return hasil

print(math())
print(math(angka_3=12))