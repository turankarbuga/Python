
sayi=int(input("Sayı Giriniz:"))
sayi = str(sayi)
liste=list(sayi)
liste1=[]
sayi=int(sayi)

üs=len(liste)

for i in str(sayi):
    i = int(i)
    liste1.append(i**üs)

if (sum(liste1)== sayi):
    print("Girilen Sayı ARMSTRONG Sayısıdır.")
else:
    print("Girilen Sayı ARMSTRONG sayısı değildir.")
