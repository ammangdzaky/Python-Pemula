# data yang dimasukka pasti string

misal = input("masukkan contoh:")
print("tipe data", misal, "adalah", type(misal))

#jika ingin int atau float, maka haru dicasting

int_ex = int(input("masukkan angka int"))
print("tipe data", int_ex, "adalah", type(int_ex))

float_ex = float(input("masukkan angka float"))
print("tipe data", float_ex, "adalah", type(float_ex))

#terus dengan boolean? harus di casting ke int agar bisa false

boolean = bool(int(input("masukkan angka int, jika bukan 0 maka true dan jika 0 maka falsep")))
print("tipe data", boolean, "adalah", type(boolean))