###### ARGS

# MEMASUKKAN BANYA DATA DENGAN CARA RIBET

def data(nama,umur,hobi):
    print(f'''
    nama : {nama}
    umur : {umur}
    hobi : {hobi}
    ''')

data("asep",12,"catur")


def data(data_biodata):
    biodata = data_biodata.copy()
    nama = biodata[0]
    umur = biodata[1]
    hobi = biodata[2]
    print(f'''
    nama : {nama}
    umur : {umur}
    hobi = {hobi}
    ''')

data(["suki", 100 , "bunuh nyamuk"])


# MEMASUKKAN BANYA DATA DENGAN ARGS

def data(*args):
    nama = args[0]
    umur = args[1]
    hobi = args[2]
    print(f'''
    nama : {nama}
    umur : {umur}
    hobi = {hobi}
    ''')

data("Fadil bayangan", 2 , "ndak tau")


# CONTOH PENGGUNAAN LAIN

def tambahkan_semua(*args:int):

    hasil = 0

    for i in args:
        hasil  += i

    return hasil

print(f"fungsi tambah menghasilkan = {tambahkan_semua(100,100,100,200)}") #menambhkan semua 100+100+100+200
