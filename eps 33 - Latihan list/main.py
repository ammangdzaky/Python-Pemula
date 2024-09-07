######### Latihan membuat databese sederhana

data_lagu = []

while True:
    print("\n")

    judul = input(f"Masukkan judul lagu : ")
    penyanyi = input(f"Masukkan nama penyanyi lagu : ")

    list_lagu = [judul,penyanyi]
    data_lagu.append(list_lagu)

    print("-"*44)
    print(f"{'No.':^4} | {"Judul":^20} | {"Penyanyi":^20}")
    print("-"*44)


    for index,lagu in enumerate(data_lagu):
        print(f"{index+1:^4} | {lagu[0]:^20} | {lagu[1]:^20}")

    lanjut = input("Ketik end jika ingin berhenti : ")

    if lanjut == "end" :
        break

print("\n" + "SELESAI".center(50,"=") + "\n")
    
    

































