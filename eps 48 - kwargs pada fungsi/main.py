## Perbedaan args dan kwargs

# ARGS   -> menggunakan list []
# KWARGS -> menggunakan dictionary {}

# args
def biodata(*args):
    nama = args[0]
    umur = args[1]
    agama = args[2]
    print(f'''
    nama  = {nama}
    umur  = {umur}
    agama = {agama}
    ''')
biodata("Asep", 12, "Islam")

# kwargs
def biodata(**kwargs):
    nama = kwargs["nama"]
    umur = kwargs["umur"]
    agama = kwargs["agama"]
    print(f'''
    nama  = {nama}
    umur  = {umur}
    agama = {agama}
    ''')
biodata(umur=12, agama="islam", nama="Asep")



### CONTOH PENGGUNAAN

def mtk(*args, **kwargs):

    hasil = 0

    if kwargs["operasi"] == "+":
        for i in args:
            hasil += i
    
    elif kwargs["operasi"] == "-":
        for i in args:
            hasil -= i

    elif kwargs["operasi"] == "*":
        hasil = 1
        for i in args:
            hasil *= i

    elif kwargs["operasi"] == "/":
        hasil = 1
        for i in args:
            hasil /= i

    else:
        print(f"Masukkan operasi yang benar (+ - * /)")

    return hasil

print(mtk(10,10,10,10,10,10,10, operasi="*"))
