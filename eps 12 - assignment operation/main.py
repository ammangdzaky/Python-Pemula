# operasi assigment merupakan operasi dengan penyingkatan
# operasi ditambah dengan assignment

a = 10  # ==> ini adalah assignment
print("nilai a adalah = ", a)

a += 3  # ==> artinya : a = a + 3
print("setelah a += 3, nilai a sekarang =", a)

a -= 4  # ==> artinya : a = a - 4
print("setelah a -= 4, nilai a sekarang =", a)

a *= 7  # ==> artinya : a = a * 7
print("setelah a *= 7, nilai a sekarang =", a)

a /= 2  # ==> artinya : a = a / 2
print("setelah a /= 2, nilai a sekarang =", a)

a %= 3  # ==> artinya : a = a % 3
print("setelah a %= 3, nilai a sekarang =", a)

a //= 3  # ==> artinya : a = a // 3
print("setelah a //= 3, nilai a sekarang =", a)

a **= 2  # ==> artinya : a = a ** 2
print("setelah a **= 2, nilai a sekarang =", a)

print("\nsemua a berurutan, misal : 9*7=63 (liat baris ke 4)")


# juga bisa dilakukan pada operasi bitwise

print("\n========bitwise=======\n")
# |
print("Or")
b = True
print("nilai b adalah ", b)
b |= True # ==> b = b | True
print("setelah b |= True, maka nilai b sekarang adalah", b)
b = True
print("nilai b adalah ", b)
b |= False # ==> b = b | False
print("setelah b |= False, maka nilai b sekarang adalah", b)

# &
print("\nAND")
b = True
print("nilai b adalah ", b)
b &= True # ==> b = b & True
print("setelah b &= True, maka nilai b sekarang adalah", b)
b = True
print("nilai b adalah ", b)
b &= False # ==> b = b & False
print("setelah b &= False, maka nilai b sekarang adalah", b)

# ^
print("\nXOR")
b = True
print("nilai b adalah ", b)
b ^= True # ==> b = b ^ True
print("setelah b ^= True, maka nilai b sekarang adalah", b)
b = True
print("nilai b adalah ", b)
b ^= False # ==> b = b ^ False
print("setelah b &= False, maka nilai b sekarang adalah", b)

