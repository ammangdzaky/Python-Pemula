#########

# Index/Urutan

#         0/-4   1/-3    2/-2     3/-1
data = ['unhas', 'unm', 'unair','unsyiah']
print(f"\ndata = {data}")

#mengambil data tertentu dari list
print("\n"+"mengambil data tertentu dari list".center(40,"-"))
print(data)
data1 = data[1]
print(f"data ke-1 (sesuai index) adalah = {data1}")
dataend = data[-1]
print(f"data terakhir adalah = {dataend}")

#mengambil info jumlah data dalam lst
print("\n"+"mengambil info jumlah dari list".center(40,"-"))
print(data)
datajumlah = len(data)
print(f"jumlah data adalah = {datajumlah}")


## MANIPULASI DATA LIST
print("\n"+"MANIPULASI DATA LIST".center(40,"=")+"\n")
print(f"data sebelum diotak atik: \n {data}")

# Menambah item pada list sesuai posisi
print("\n"+"menambah item pada list sesui posisi".center(40,"-"))
data.insert(0,"itb") #urutan elemen
print(f"setelah: \n {data}")

# Menambah diakhir list
print("\n"+"menambah diakhir list".center(40,"-"))
data.append("pnup") #
print(f"setelah: \n {data}")

# Menambah list dengan list
print("\n"+"menambah list dengan k=list".center(40,"-"))
datanew = ["ui",'umi']
data.extend(datanew) 
print(f"setelah: \n {data}")

# MMerubah data
print("\n"+"merubah data".center(40,"-"))
data[0] = "rubah"
print(f"setelah data 0 dirubah: \n {data}")

# "meremove data
print("\n"+"meremove data".center(40,"-"))
data.remove("rubah")
print(f"setelah: \n {data}")

# "meremove data paling akhir
print("\n"+"meremove data paling akhir".center(40,"-"))
data.pop()
print(f"setelah: \n {data}")





