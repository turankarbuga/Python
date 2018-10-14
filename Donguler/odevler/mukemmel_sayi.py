
sayi=int(input("Sayı Giriniz:"))

bolenler = []

for i in range(1,sayi):
    if (sayi % i == 0):
        bolenler.append(i)
print(bolenler)

if(sum(bolenler)==sayi):
    print("Girilen sayı MÜKEMMEL!")
else:
    print("Maalesef mükemmel sayı değil")
