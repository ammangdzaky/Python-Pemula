# operasi komparasi artinya membandingkan bilangan
# hasil dari comparison operation adalah boolean
# >, <, >=, <=, ==, is, is not

a = 2
b = 4

# lebih besar dari (>)
result = a > 3
print("hasil dari", a, "> 3 adalah :", result)
result = b > 3
print("hasil dari", b, "> 3 adalah :", result)
result = a > 2
print("hasil dari", a, "> 2 adalah :", result)

# lebih kecil dari (<)
result = a < 3
print("hasil dari", a, "< 3 adalah :", result)
result = b < 3
print("hasil dari", b, "< 3 adalah :", result)
result = a < 2
print("hasil dari", a, "< 2 adalah :", result)

# lebih besar sama dengan (>=)
result = a >= 3
print("hasil dari", a, ">= 3 adalah :", result)
result = b >= 3
print("hasil dari", b, ">= 3 adalah :", result)
result = a >= 2
print("hasil dari", a, ">= 2 adalah :", result)

# lebih kecil sama dengan (<=)
result = a <= 3
print("hasil dari", a, "<= 3 adalah :", result)
result = b <= 3
print("hasil dari", b, "<= 3 adalah :", result)
result = a <= 2
print("hasil dari", a, "<= 2 adalah :", result)

#  sama dengan (==)
result = a == 3
print("hasil dari", a, "== 3 adalah :", result)
result = b == 3
print("hasil dari", b, "== 3 adalah :", result)
result = a == 2
print("hasil dari", a, "== 2 adalah :", result)

#  tidak sama dengan (!=)
result = a != 3
print("hasil dari", a, "!= 3 adalah :", result)
result = b != 3
print("hasil dari", b, "!= 3 adalah :", result)
result = a != 2
print("hasil dari", a, "!= 2 adalah :", result)


# is dan is not  ---> mirip == dan != tapi digunakan untuk membandingkan 2 variable
# a is 4 (ini tidak boleh)
# a is b (ini boleh)
# b is not a (ini boleh)

a = 5
b = 3

# is
result = a is b
print("hasil dari", a, "is", b, "adalah :", result)
result = a is a
print("hasil dari", a, "is", a, "adalah :", result)
result = b is b
print("hasil dari", b, "is", b, "adalah :", result)

# is not
result = a is not b
print("hasil dari", a, "is not", b, "adalah :", result)
result = a is not a
print("hasil dari", a, "is not", a, "adalah :", result)
result = b is not b
print("hasil dari", b, "is not", b, "adalah :", result)

