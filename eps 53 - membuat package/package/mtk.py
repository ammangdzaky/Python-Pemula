def tambah(*args:int):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kurang(*args:int):
    hasil = 0
    for i in args:
        hasil -= i
    return hasil

def kali(*args:int):
    hasil = 1
    for i in args:
        hasil *= i
    return hasil

def bagi(*args:int):
    hasil = 1
    for i in args:
        hasil /= i
    return hasil

def pangkat(n):
    return lambda angka : angka**n

