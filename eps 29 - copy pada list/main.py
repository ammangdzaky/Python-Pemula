# tutorial mengcopy/duplikat list

a = ['unm', 'unhas', 'umi']
print(f"a = {a}")

b = a # ini sebetulnya tidak menduplikat list a, karena jika b diubah maka a juga berubah
print(f"b = {b}") 

print(f"addreas a = {hex(id(a))}")
print(f"addreas b = {hex(id(b))}")

print("saya ubah b maka pasti a berubah")
b[0] = "uin"
print(a)
print(b)
print("tuhkan")

#########################

print(f"\ntutorial duplikat list===========") # menggunakan b = ca.copy()


a = ['unm', 'unhas', 'umi']
print(f"a = {a}")

b = a.copy()
print(f"b = {b}") 

print(f"addreas a = {hex(id(a))}")
print(f"addreas a = {hex(id(b))}")

print("saya ubah b maka pasti a tidak berubah")
b[0] = "uin"
print(a)
print(b)
print("duplikat berhasil")