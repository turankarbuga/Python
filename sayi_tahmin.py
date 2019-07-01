

print("""********************
sayı tahmin oyunu v1.0

********************

""")


import random
import time

rastgele_sayi=random.randint(1,40)
tahmin_hakki=7

while True:
    tahmin=int(input("Tahmininiz:"))

    if(tahmin<rastgele_sayi):
        print("Lütfen bekleyin..")
        time.sleep(0.75)

        print("Daha büyük")
        tahmin_hakki -=1
    elif(tahmin>rastgele_sayi):
        print("Lütfen bekleyin..")
        time.sleep(0.75)

        print("Daha küçük")
        tahmin_hakki-=1
    else:
        print("Lütfen bekleyin..")
        time.sleep(0.75)

        print("Tebrikler! Doğru sayı:",rastgele_sayi)
        break

    if(tahmin_hakki==0):
        print("tahmin hakkınız bitmiştir. Oyunu tekrar başlatınız. Doğru sayı:",rastgele_sayi)
        break
