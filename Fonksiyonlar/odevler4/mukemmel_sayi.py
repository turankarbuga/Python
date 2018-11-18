print('''
************************

1'den 1000'e kadar olan mükemmel sayılar 

************************
''')

def mukemmel_sayi(sayi):
    tam_bolenler=[]
    for i in range(1,sayi):
        if(sayi%i == 0):
            tam_bolenler.append(i)

    toplam=sum(tam_bolenler)
    if (toplam == sayi):
        print(sayi,"mükemmel bir sayıdır.")


for j in range(1,1001):
    mukemmel_sayi(j)

