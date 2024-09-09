### Copy and POP
# pop -> mengambil data dan mengeluarkannya dari dict

dict = {
    1 : "one",
    2 : "two",
    3 : "three"
}


## Copy 
print("="*20)

dictionary = dict.copy()

print(f"dict = {dict}")
print(f"dictionary = {dictionary}")


## pop -> berdasarkan key
print("="*20)

pop = dict.pop(1)
print(pop)
print(dict)

## popitem -> mengambil yang terakhir -> mengambil key and value
print("="*20)

popitem = dict.popitem()
print(popitem)
print(dict)

