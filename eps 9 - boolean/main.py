# not, or, and, xor


# NOT ==> mirip seperti negasi/kebalikan
print('=====NOT=====')
a = True
b = False
c = not a
d = not b
print ("jika not true, maka hasilnya = ", c)
print ("jika not false, maka hasilnya = ", d)

# OR ==> bernilai true jika ada yang true
print("====OR====")
a = True
b = True
c = a or b
print(a, "OR", b, "hasilnya =", c)
a = True
b = False
c = a or b
print(a, "OR", b, "hasilnya =", c)
a = False
b = True
c = a or b
print(a, "OR", b, "hasilnya =", c)
a = False
b = False
c = a or b
print(a, "OR", b, "hasilnya =", c)

# AND ==> bernilai true jika semua true
print("====AND====")
a = True
b = True
c = a and b
print(a, "AND", b, "hasilnya =", c)
a = True
b = False
c = a and b
print(a, "AND", b, "hasilnya =", c)
a = False
b = True
c = a and b
print(a, "AND", b, "hasilnya =", c)
a = False
b = False
c = a and b
print(a, "AND", b, "hasilnya =", c)

# XOR (^ or press shift+6) ==> bernilai true hanya 1 yang true
print("====XOR====")
a = True
b = True
c = a ^ b
print(a, "XOR", b, "hasilnya =", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "hasilnya =", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "hasilnya =", c)
a = False
b = False
c = a ^ b
print(a, "XOR", b, "hasilnya =", c)


print("===========")
a = True
b = True
c = False
d = a or b or c

print(d)


