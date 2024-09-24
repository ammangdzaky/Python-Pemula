### Ini adalah module dengan nama matematika

def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kurang(*args):
    hasil = 0
    for i in args:
        hasil -= i
    return hasil

def kali(*args):
    hasil = 1
    for i in args:
        hasil *= i
    return hasil

def bagi(*args):
    hasil = 1
    for i in args:
        hasil /= i
    return hasil

    
def pangkat(num):
    hasil = lambda angka : angka**num
    return hasil