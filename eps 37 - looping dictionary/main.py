# looping dictionary

dict = {
    1 : "satu",
    2 : "dua",
    3 : "tiga",
    4 : "empat",
    5 : "lima"
}

print(f'''
Dictionary:
{dict}
''')


print("\n"+"="*20) 


## mengambil key
key = dict.keys()
print(key)

for i in dict.keys():
    print(i)


print("\n"+"="*20) 


## Mengambil Values
value = dict.values()
print(value)

for i in dict.values():
    print(i)


print("\n"+"="*20) 


## Mengambil Key dan Values
item = dict.items()
print(item)

for i in dict.items():
    print(i)

for key,value in dict.items():
    print(f"key = {key}  ,  value = {value}")

