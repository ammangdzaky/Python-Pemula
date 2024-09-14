import os
os.system("cls")

''' output = lambda argument : expression '''

# LAMBDA UNTUK MEMBUAT LEBIH SINGKAT

# menggunakan fungsi
def kuadrat(angka):
    return angka**2
print(f"kuadrat 3 dengan fungsi = {kuadrat(3)}")

# menggunakan lambda
kuadrat = lambda nilai : nilai**2 #syntaxnya lebih sederhana
print(f"kuadrat 3 dengan lambda = {kuadrat(3)}")

pangkat = lambda angka, pangkat : angka**pangkat
print(f"pangkat dengan lambda = {pangkat(3,3)}\n\n")


############ GUNA LAMBDA APA????????????



#######SORTING

### -> sorting biasa
data = ["dudul", "aaaaaaa" , "sukiii", "afahiya"]
data.sort()
print(data)

# sorting berdasarkan panjang
data = ["dudul", "aaaaaaa" , "sukiii", "afahiya"]
data.sort(key=len)
print(f"biasa = {data}")

# sorting berdasarkan panjang pake fungsi
data = ["dudul", "aaaaaaa" , "sukiii", "afahiya"]

def panjang(nama):
    return len(nama)

data.sort(key=panjang)
print(f"fungsi = {data}")

# sorting berdasarkan panjang pake lambda
data = ["dudul", "aaaaaaa" , "sukiii", "afahiya"]
data.sort(key = lambda nama : len(nama))
print(f"lambda = {data}\n\n")



#######FILTER

malas = [1,2,3,4,55,6,33,100,0,4,5,5,5121]

## filter jika lebih dari 10

#pake fungsi(cupu)

def lebih10(x):
    return x > 10

data = list(filter(lebih10, malas)) # -> filter(apa filternya , data yang difilter)
print(f"cupu = {data}")


# pake lambda (pro bjir)
pro = list(filter(lambda x : x > 10, malas))
print(f"pro = {pro}")

# lambda genap
genap = list(filter(lambda x : x % 2 == 0, malas))
print(f"pro genap = {genap}")

# lambda ganjil 
ganjil = list(filter(lambda x : x % 2 != 0, malas))
print(f"pro ganjil = {ganjil}")

# lambda kelipatan 5
kelipatan_5 = list(filter(lambda x : x % 5 == 0, malas))
print(f"pro kelipatan 5 = {kelipatan_5}")



