### FUNGSI DENGAN RETURN

# def fungsi(argument):
#     '''keterangan'''
#     body fungsi
#     return output


def kali(angka_1,angka_2):
    '''fungsi tambah'''
    return angka_1 * angka_2

print(kali(9,9)) #-->

##########

def kuadrat(angka):
    '''fungsi kuadrat'''
    hasil = angka**2
    return hasil

print(kuadrat(9)) #-->

########## MISAL JIKA BANYAK RETURN

def math(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

a = math(10,5) #-->

print(a)


# ATAU

b,c,d,e = math(10,5)

print(b) #-->
print(c) #-->
print(d) #-->
print(e) #-->



