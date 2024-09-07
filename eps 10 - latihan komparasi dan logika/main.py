op = input('apakah kamu siap,\n ketik apa saja untuk melanjutkan:')


# kita akan buat ----0++++5----8++++11----
# artinya x akan true jika 0>=x<=5 dan 8>=x<=11

print("\n----0++++5----8++++11----\n")
print("masukkan nilai x dengan syarat\n a. 0>=x<=5\n b. 8>=x<=11")
print("(pastikan hanya memasukkan angka)")
answer = float(input("x = "))

benar1 = answer >= 0
benar11 = answer <= 5
benar111 = benar1 and benar11

benar2 = answer >= 8
benar22 = answer <= 11
benar222 = benar2 and benar22

hasil = benar111 or benar222

print("nilai x yang kamu masukkan", hasil)

print("\n",20*"=","\n")


# kita akan buat ++++0----5++++8----11++++
# x true if x<=0, 5<=x<=8, 1x>=11

print("masukkan nilai x dengan syarat\n a. x<=0\n b. 5<=x<=8\n c. x>=11")
print("(pastikan hanya memasukkan angka)")
user = float(input("x = "))

syarat = user <= 0 or 5<=user<=8 or 11 <= user
print("nilai x yang kamu masukkan", syarat)

