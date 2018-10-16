
print('''
****************************
Faktoriyel v1.0
****************************

ÇIKMAK İÇİN X'E BASIN

''')
while True:
    sayi=input("Sayı Giriniz:")
    if(sayi=="x"):
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*=i
    print("{}! = {}".format(sayi,faktoriyel))

