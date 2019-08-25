from kütüphane import *

print("""
1-Kitapları Göster
2-Kitap Sorgula
3-Kitap Ekle
4-Kitap Sil
5-Baskı Yükselt

Çıkmak için 'q'ya basınız.
""")

kutuphane = Kutuphane()

while True:
    islem = input("İşlem seçiniz:")

    if (islem == 'q'):
        print("Çıkış yapılıyor...")
        break
    elif(islem == '1'):
        print("Kitaplar getiriliyor...")
        sleep(1)
        kutuphane.kitaplari_goster()
    elif (islem == '2'):
        isim = input("Kitap ismi:")
        kutuphane.kitap_sorgula(isim)
    elif (islem == '3'):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))

        print("Kitap ekleniyor...")
        sleep(2)

        kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        kutuphane.kitap_ekle(kitap)
        print("Kitap eklendi.")

    elif (islem == '4'):
        isim = input("Silmek istediğiniz kitabın ismi:")
        cevap = input("Emin misiniz? (Y/N):")

        if (cevap == 'Y' or 'y'):
            print("Kitap siliniyor...")
            sleep(2)
            kutuphane.kitap_sil(isim)
            print("{} isimli kitap silindi.".format(isim))

        else:
            print("Silme işlemi iptal edildi.")

    elif (islem == '5'):
        isim = input("Baskısı yükseltilecek olan kitabın ismi:")

        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltiliyor...")
        sleep(2)
        print("Baskı yükseltildi.")


    else:
        print("Geçersiz işlem.")
