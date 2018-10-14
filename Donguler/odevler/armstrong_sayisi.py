sayi=int(input("Sayı Giriniz:"))
sayi=str(sayi)
üs=len(sayi)
sayi=int(sayi)
liste=[]

for i in str(sayi):
    i = int(i)
    liste.append(i**üs)

if (sum(liste)== sayi):
    print("Girilen Sayı ARMSTRONG Sayısıdır.")
else:
    print("Girilen Sayı ARMSTRONG sayısı değildir.")
