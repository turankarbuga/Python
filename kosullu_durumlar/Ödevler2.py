#problem1
"""
kilo=float(input("Kilo(kg):"))
boy=float(input("Boy(cm):"))
bki= kilo / (boy/100*boy/100)

print(bki)

if (bki<18.5):
    print("Zayıf")
elif(18.5<bki<25):
    print("Normal")
elif("25<bki<30"):
    print("Kilolu")
else:
    print("Obez")
"""

#problem2
""""
print(" karşılaştırmak istediğiniz sayıları giriniz.")

sayı1=float(input("Sayı 1:"))
sayı2=float(input("Sayı 2:"))
sayı3=float(input("Sayı 3:"))

if (sayı1>sayı2 and sayı1>sayı3):
    print("en büyük sayı {}".format(sayı1))

elif(sayı2>sayı1 and sayı2>sayı3):
    print("en büyük sayı {}".format(sayı2))
else:
    print("en büyük sayı {}".format(sayı3))  
"""

#problem3
"""
print("***NOT HESAPLAMA***")
vize1=float(input("Vize 1 notunuz:"))
vize2=float(input("Vize 2 notunuz:"))
final=float(input("Final notunuz:"))

toplam_not=(vize1*3/10)+(vize2*3/10)+(final*4/10)

if(toplam_not >=  90):
    print("Notunuz AA")
elif (toplam_not  >=  85 ):
    print("Notunuz BA")
elif (toplam_not >= 80):
    print("Notunuz BB")
elif (toplam_not >= 75):
    print("Notunuz CB")
elif (toplam_not  >=  70 ):
    print("Notunuz CC")
elif (toplam_not  >=  65 ):
    print("Notunuz DC")
elif (toplam_not  >=  60 ):
    print("Notunuz DD")
elif (toplam_not >= 55):
    print("Notunuz FD")
else:
    print("Notunuz FF")
"""

#problem4
"""
print('''
Hangi geometrik şeklin tipini bulmak istiyorsunuz? 

Üçgen için 3;
Dörtgen için 4 yazınız.
''')
şekil=int(input("Şekil:"))

if(şekil==3):
    print("Kenarları yazınız.")
    kenar1=float(input("Kenar 1:"))
    kenar2=float(input("Kenar 2:"))
    kenar3=float(input("Kenar 3:"))

    if(kenar1+kenar2>kenar3>abs(kenar1-kenar2) or kenar1+kenar3>kenar2>abs(kenar1-kenar3) or kenar2+kenar3>kenar1>abs(kenar2-kenar3)):
        if (kenar1 == kenar2 == kenar3):
            print("Girilen üçgen EŞKENAR üçgendir.")
        elif (kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3):
            print("Girilen üçgen İKİZKENAR üçgendir.")
        else:
            print("Girilen üçgen ÇEŞİTKENAR üçgendir.")

    else:
        print("Girilen sayılardan bir üçgen oluşturulamaz!")

if(şekil==4):
    print("Kenarları saat yönüne göre yazınız.(Unutmayın tüm açılar 90 derece kabul edilecektir.)")
    a = float(input("Kenar 1:"))
    b = float(input("Kenar 2:"))
    c = float(input("Kenar 3:"))
    d = float(input("Kenar 4:"))
    if(a==c and b==d and a!=b):
        print("Girilen şekil DİKDÖRTGEN.")
    elif(a==b==c==d):
        print("Girilen şekil KARE.")
    else:
        print("Açıları 90 derece olan bir dörtgen belirtmez.")

else:
    print("3 ya da 4 giriniz.")
"""
