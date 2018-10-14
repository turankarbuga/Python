
print('''
ATM PROGRAMI v1.0

İŞLEMLER:
1-Bakiye Sorgula
2-Para Yatır
3-Para Çek
4-Çıkış Yap
''')

bakiye= 5000

while True:
    işlem=int(input("İşlem Giriniz:"))

    if (işlem==1):
        print(bakiye)
    elif (işlem==2):
        miktar=int(input("Yatırmak istediğiniz miktar:"))
        bakiye+=miktar
        print("---İşlem Gerçekleştiriliyor... \n---İşlem Gerçekleştirildi.")
        print("Mevcut Bakiye:{}".format(bakiye))
    elif(işlem==3):
        miktar = int(input("Çekmek istediğiniz miktar:"))
        if(miktar>bakiye):
            print("Hesabınızda bulunan miktar {} olduğu için girilen miktarda para çekemezsiniz.".format(bakiye))
            continue
        bakiye -= miktar
        print("---İşlem Gerçekleştiriliyor... \n---İşlem Gerçekleştirildi.")
        print("Mevcut Bakiye:{}".format(bakiye))
    elif(işlem==4):
        print("Çıkış yapılıyor...")
        break

