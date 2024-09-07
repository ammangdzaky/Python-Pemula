# didalam list boleh ada list

a = [1,2]
b = ['ucup','otong']
listt = [a,b,'rudi',3]

print(listt)

# contoh penggunaan 
print("===========")

a = ["asep",10,"catur"]
b = ["alan",12,"memasak"]
c = ["kiki",11,"menari"]

peserta = [a,b,c]

for i in  peserta:
    print(f"nama : {i[0]}")
    print(f"umur : {i[1]}")
    print(f"hobi : {i[2]} \n")
