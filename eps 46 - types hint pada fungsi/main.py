###### TYPES HINT

# study case

'''
def kuadrat(angka):
    return angka**2
print(kuadrat(10))  # KETIKA DIHOVER : any -> any
print(kuadrat("huruf")) # KETIKA DIHOVER : any -> any
'''

def kuadrat(angka:int):
    return angka**2

print(kuadrat(100)) #KETIKA kuadrat() dihover : int -> int
print(kuadrat("huruf")) #ketika kuadrat() dihover : int -> int