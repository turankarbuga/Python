
from math import factorial
from math import sin
from math import cos
from math import tan
from math import log
from math import sqrt
from time import sleep
from math import pi


print("""**************************
Hesap Makinesi v2.0
**************************""")

print("""~*~*~*İŞLEM SEÇİNİZ*~*~*~

    1-TOPLAMA
    2-ÇIKARMA
    3-ÇARPMA
    4-BÖLME
    5-ÜS ALMA
    6-KAREKÖKÜNÜ ALMA
    7-LOGARİTMA
    8-FAKTÖRİYEL
    9-SİN
    10-COS
    11-TAN

    ÇIKMAK İÇİN ÇIKIŞ YAZINIZ.

    """)


while True:

    islem=input("İşlem Numarası giriniz:")

    if(islem=="ÇIKIŞ"):
        print("Programdan çıkış yapılıyor...")
        sleep(1)
        break
    elif(islem=='1'):
        print("""Sayıları Giriniz. Sayıları girdikten sonra toplama yapmak için x tuşuna basınız.""")
        toplama_listesi = []

        while True:
            sayilar=input("Sayı:")

            if(sayilar=="x"):
                toplam=sum(toplama_listesi)
                print("Girilen sayıların toplamı {}".format(toplam))
                break
            else:
                sayilar=int(sayilar)
                toplama_listesi.append(sayilar)

    elif(islem=='2'):

        sayi1=int(input("Sayı 1:"))
        sayi2=int(input("Sayı 2:"))

        cikarma=sayi1-sayi2
        print("Girilen sayıların farkı {}".format(cikarma))

    elif(islem=='3'):

        carpma_listesi=[]

        while True:

            sayilar=input("Sayı:")

            if(sayilar=="x"):

                def carpma(carpma_listesi):
                    sonuc = 1
                    for i in carpma_listesi:
                        sonuc= sonuc * i

                    return sonuc

                print("Girilen sayıların çarpımı {}".format(carpma(carpma_listesi)))



                break

            else:
                sayilar=int(sayilar)

                carpma_listesi.append(sayilar)

    elif(islem=='4'):

        sayi1 = int(input("Sayı 1:"))
        sayi2 = int(input("Sayı 2:"))

        bolum=sayi1/sayi2
        print("Girilen sayıların bölümü {}".format(bolum))

    elif(islem=='5'):

        taban=float(input("Taban:"))
        us=float(input("Üs:"))

        sonuc=taban**us

        print("{} üzeri {} = {}".format(taban,us,sonuc))

    elif(islem=='6'):

        sayi=float(input("Karekökünü almak istediğiniz sayı:"))

        if(sayi<0):
            print("Karekök alma işleminde negatif sayılar kullanılamaz.")

        else:

            print("{} sayısının karekökü {}".format(sayi,sqrt(sayi)))

    elif(islem=='7'):


        taban=float(input("Taban:"))

        if(taban<=0 or taban ==1):
            print("Logaritma fonksiyonunnda taban 0'dan küçük veya eşit ve 1'e eşit olamaz.")
            break


        sayi=float(input("Sayı:"))

        if(sayi<=0):
            print("Logaritma fonksiyonunda logaritması alınacak olan sayı 0'dan büyük olmaz zorunda.")
            break

        else:
            print("{} tabanında {} işleminin sonucu {}".format(taban,sayi,log(sayi,taban)))

    elif(islem=='8'):

        sayi=int(input("Faktöriyeli alınacak sayı:"))

        if(sayi<0):
            print("Faktöriyeli alınacak sayı negatif olamaz.")

        else:
            print("{} sayısının faktöriyeli {}".format(sayi,factorial(sayi)))

    elif(islem=='9'):

        print("""
        işleminizi radyan cinsinden mi yoksa derece cinsinden mi yapmak istersiniz? 
        
        1-Radyan
        2-Derece     
           
        """)
        secim=int(input("seçiminiz:"))

        if(secim==1):

            sayi_radyan=float(input("radyan cinsinden sinüsü alınacak sayı:"))

            print("{} açısının sinüsü {}".format(sayi_radyan,sin(sayi_radyan)))

        elif(secim==2):

            sayi_derece=float(input("Derece cinsinden sinüsü alınacak sayı:"))

            sayi_derece_donustur=sayi_derece*pi/180

            print("{} açışının sinüsü {}".format(sayi_derece,sin(sayi_derece_donustur)))


    elif(islem=='10'):

        print("""
                işleminizi radyan cinsinden mi yoksa derece cinsinden mi yapmak istersiniz? 

                1-Radyan
                2-Derece     

                """)
        secim = int(input("seçiminiz:"))

        if (secim == 1):

            sayi_radyan = float(input("radyan cinsinden cosinüsü alınacak sayı:"))

            print("{} açısının cosinüsü {}".format(sayi_radyan, cos(sayi_radyan)))

        elif (secim == 2):

            sayi_derece = float(input("Derece cinsinden cosinüsü alınacak sayı:"))

            sayi_derece_donustur = sayi_derece * pi / 180

            print("{} açışının sinüsü {}".format(sayi_derece, cos(sayi_derece_donustur)))

    elif(islem=='11'):

        print("""
                işleminizi radyan cinsinden mi yoksa derece cinsinden mi yapmak istersiniz? 

                1-Radyan
                2-Derece     

                        """)
        secim = int(input("seçiminiz:"))

        if (secim == 1):

            sayi_radyan = float(input("radyan cinsinden tanjantı alınacak sayı:"))

            print("{} açısının tanjantı {}".format(sayi_radyan, tan(sayi_radyan)))

        elif (secim == 2):

            sayi_derece = float(input("Derece cinsinden tanjantı alınacak sayı:"))

            sayi_derece_donustur = sayi_derece * pi / 180

            print("{} açışının tanjantı {}".format(sayi_derece, tan(sayi_derece_donustur)))

    else:

        print("Hatalı işlem numarası lütfen tekrar yazınız.")




















