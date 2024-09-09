## Operasi Dictionary

dict = {
    1 : "satu",
    2 : "dua",
    3 : "tiga"
}

print(f"""
Dictionary awal yaitu :
{dict}
""")

print("\n"+"="*20)

# panjang dicitonary
panjang = len(dict)
print(f"panjang {dict} yaitu : {panjang}")

print("\n"+"="*20)

# mengecek key ada atau tidak
key = 4
check = key in dict
print(f"apakah {key} ada di dict : {check}")

print("\n"+"="*20)

# mengakses value dengan get
print(dict[1]) # -> tidak menggunakan get
print(dict.get(1)) # -> menggunakan get
print(dict.get(4)) # -> none
print(dict.get(4, "tidak ditemukan")) # -> mengganti none dengan tidak ditemukan

print("\n"+"="*20)

# mengupdate data   
# -> mengubah data
dict[1] = "one" # > tidak menggunakan update
dict.update({2 : "two"}) # > menggunakan update
print(dict)
# -> menambahkan data baru
dict[4] = "empat" # > tdk menggunakan update
dict.update({5 : "lima"}) # > menggunakan update
print(dict)

print("\n"+"="*20)

# mendelete data pada dict
del dict[4]
del dict[5]
print(dict)