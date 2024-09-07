##
print("\n")


# melihhat berapa kali data muncul dalam list -> .count
print("\n")
data = [1,2,1,2,1,2,2,3,4,32,4,3,4,4,5,9,7]
print(data)
count = data.count(2)
print(f'angka 2 muncul sebanyak = {count}')


# melihat posisi data/ index -> .index
print("\n")
data = ["abdul","dudul","dullah"]
print(data)
dudul = data.index("dudul")
print(f"index si dudul yaitu = {dudul}")


# mengurutkan list -> .sort
print("\n")
data = [1,2,1,2,1,2,2,3,4,32,4,3,4,4,5,9,7]
print(f"sebelum : {data}")
data.sort()
print(f"setelah : {data}")
data = ["dudul","dullah","abdul"]
print(f"sebelum : {data}")
data.sort()
print(f"setelah : {data}")

# membalik urutan list -> .reverse
# untuk membalik urutan. harus di sort kemudian di reverse
print("\n")
data = [1,2,1,2,1,2,2,3,4,32,4,3,4,4,5,9,7]
print(f"sebelum : {data}")
data.sort()
data.reverse()
print(f"setelah : {data}")
data = ["abdul","dullah","dudul"]
print(f"sebelum : {data}")
data.sort()
data.reverse()
print(f"setelah : {data}")