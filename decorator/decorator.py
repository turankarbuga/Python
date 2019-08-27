def ekstra(func):
    def wrapper(sayilar):

        tek_sayilar=list()
        cift_sayilar=list()

        for i in sayilar:
            if (i % 2 == 0):
                cift_sayilar.append(i)
            else:
                tek_sayilar.append(i)
        print("Tek Sayıların Ortalaması ",sum(tek_sayilar)/len(tek_sayilar))
        print("Çift Sayıların Ortalaması ",sum(cift_sayilar)/len(cift_sayilar))
        func(sayilar)
    return wrapper


@ekstra
def ortalama_hesapla(sayilar):

    ortalama = (sum(sayilar)/len(sayilar))
    print("Genel Ortalama : {}".format(ortalama))

ortalama_hesapla([50,55,60,30,40,85,75,100,90,80,100])

