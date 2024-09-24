def ganjil(list:int):
    hasil = []
    for i in list:
        if i % 2 != 0:
            hasil.append(i)
    return hasil

def genap(list):
    hasil = []
    for i in  list:
        if i % 2 == 0:
            hasil.append(i)
    return hasil

def prima(list):
    hasil = []
    for i in list:
        if i > 1:
            is_prima = True
            for num in range(2,i):
                if i % num == 0:
                    is_prima = False
                    break
            if is_prima:
                hasil.append(i)
    return hasil





