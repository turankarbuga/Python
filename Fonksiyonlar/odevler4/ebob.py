sayi1=int(input("Sayı 1:"))
sayi2=int(input("Sayı 2:"))
liste=[]

def ebob(sayi1,sayi2):

    for i in range(1,sayi2+1):
        if(sayi1 % i == 0 and sayi2%i==0):
            liste.append(i)

    return liste[-1]



print(ebob(sayi1,sayi2))