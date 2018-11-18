print("Çıkmak için x'e basınız.")

def asal_sayi(sayi):
    if sayi==1:
        return False
    elif sayi==2:
        return True
    elif sayi<1:
        return False
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return True

while True:
    sayi = input("Sayıyı Giriniz:")

    if(sayi=="x"):
        break
    else:
        sayi = int(sayi)
        if(asal_sayi(sayi)):
            print(sayi,"asal bir sayıdır.")
        else:
            print(sayi,"asal bir sayı değildir.")
