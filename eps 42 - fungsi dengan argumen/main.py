## FUNGSI DENGAN ARGUMEN



# def fungsi(arguments):
#     '''keterangan fungsi'''
#     BADAN FUNGSI 


def tentang_aku(nama):
    '''fungsi mengatakan aku baik'''
    print(f"{nama} rajin belajar")
    print(f"{nama} rajin menabung")
    print(f"{nama} rajin membantu")

tentang_aku("dzaky")


print("="*20)  ## NEXT


def perkalian(angka1,angka2):
    '''fungsi untuk perkalian'''
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} = {hasil}")

perkalian(111,23)
perkalian("aku",10)


print("="*20)  ## NEXT


def peserta(nama):
    Nama = nama.copy()
    for i in Nama:
        print(f"Selamat datang {i} di lokasi UTBK")


Peserta = ["dzaky", "ucup", "dudung"]
Peserti = ["jamili", "mulyini", "hartini"]

peserta(Peserta)
peserta(Peserti)
