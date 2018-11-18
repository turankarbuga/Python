
def tam_bolenler(sayi):
    tambolen=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            tambolen.append(i)
    return tambolen

while True:
    sayi=input("Sayı:")

    if(sayi=="x"):
        break
    else:
        sayi=int(sayi)
        print("Tam bölenler:",tam_bolenler(sayi))
