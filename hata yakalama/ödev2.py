
def tek_cift(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError


liste=[1,98,3,77,24,51,49,13,44,62]

for sayi in liste:
    try:
        print(tek_cift(sayi))
    except ValueError:
        pass
