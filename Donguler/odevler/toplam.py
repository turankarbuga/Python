print('''
Girilen sayıları toplar.
Çıkmak için 'q'ya basınız.

''')


toplam=0

while True:
    sayi = input("Sayı:")
    if(sayi=="q"):
        print(toplam)
        print("Çıkış yapılıyor...")
        break
    else:
        sayi=int(sayi)
        toplam += sayi
        print(toplam)
