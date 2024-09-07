## --- LIST ---

# Kumpulan data numbers
print("kumpulan data numbers")
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
print("Kumpulan data string")
data_string = ["ucup","otong","odah"]
print(data_string)

# Kumpulan data boolean
print("Kumpulan data boolean")
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
print("Kumpulan campuran")
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)

## cara alternatif membuat list
print("range")
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
print("for")
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)
list_pake_for = [i**2 for i in range(0,10)] # -> ini membuat dikuadratkan 2
print(list_pake_for)

# membuat list pake for pake if
print("for dan if")
list_pake_for_if = [i for i in range(0,10) if i != 5] # -> ini artinya angka 5 tidak diprint
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0] # -> print genap
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0] # -> print ganjil kemudian dikuadratkan
print(list_pake_for_if)