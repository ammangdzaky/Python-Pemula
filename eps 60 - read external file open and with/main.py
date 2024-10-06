import os
os.system("cls")
os.chdir("C:/Users/Dzaky/Documents/Python Pemula/eps 60 - read external file open and with")
# diatas untuk mengganti folder kerjanya ke eps 60 bla bla agar file data.txt dapat ditemukan


# sebelum membaca atau menulid sebuah file, maka kita harus membuka (open) file terlebih dahlu
# setelah file fiopen, maka harus di close

print("pengantar".center(20, "="))

file = open("data.txt",mode="r") # r -> read
print(f"status read = {file.readable()}")
print(f"status write = {file.writable()}") # -> false karna diatas r, bukan w

print(file.read())
print(file.readlines()) # -> ini tidak akan terbaca (kosong) karna filenya harus ditutup dulu
# satu perintah hanya untuk satu kali open
print(f"apakah sudah ditutup = {file.closed}")
file.close()
print(f"apakah sudah ditutup = {file.closed}")

file = open("data.txt",mode="r")
print("\n",file.readlines(),"\n") # -> ini tidak akan terbaca (kosong) karna filenya harus ditutup dulu



##### OPEN
print("read dengan (open)".center(40,"="))

# membaca semua yang ada di dalam file -> read()
print(f"\nread()")
file = open("data.txt",mode="r")
print(file.read (),"\n")
file.close()

# membaca baris perbaris -> readline()
print("readline()")
file = open("data.txt",mode="r")
print(file.readline()) # -> baris pertama
print(file.readline(),end="") # -> baris kedua dan \n dihilangkan dengan " "
print(file.readline(),"\n") # -> baris pertama
file.close()

# membaca semua yang ada di dalam file sebagai list -> readlines()
print(f"readlines()")
file = open("data.txt",mode="r")
print(file.readlines ())
file.close()



###### WITH
print('\n\n',"read dengan (with)".center(40,"="))

with open("data.txt",mode="r") as file:
    print(f"status close = {file.closed}")

print(f"status close = {file.closed}\n\n")


# membaca semua yang ada di dalam file -> read()
print(f"\nread()")
with open("data.txt",mode="r") as file:
    print(file.read(),"\n\n")
    
# membaca baris perbaris -> readline()
print(f"readline()")
with open("data.txt",mode="r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
# membaca semua sebagai list -> readlines()
print(f"\n\nreadlines()")
with open("data.txt",mode="r") as file:
    print(file.readlines(),"\n\n")


