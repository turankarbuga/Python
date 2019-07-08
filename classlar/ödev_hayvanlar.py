import time

class Hayvanlar():
    def __init__(self,yasam_yeri,beslenme,tur):

        self.yasam_yeri=yasam_yeri
        self.beslenme=beslenme
        self.tur=tur

    def __str__(self):
        return "Hayvanlar Alemi"

class Kuslar(Hayvanlar):
    def __init__(self,yasam_yeri,beslenme,tur,ayak_sayisi,ortalama_omur,ureme):
        super().__init__(yasam_yeri,beslenme,tur)
        self.ayak_sayisi=ayak_sayisi
        self.ortalama_omur=ortalama_omur
        self.ureme=ureme

    def bilgileri_goster(self):
        print ("""
        Yaşam Yeri: {}
        Beslenme Şekli: {}
        Türü: {}
        Ayak Sayısı: {} adet
        Ortalama Ömrü: {} 
        Üreme Şekli: {}
        """.format(self.yasam_yeri,self.beslenme,self.tur,self.ayak_sayisi,self.ortalama_omur,self.ureme))


class Kopekler(Hayvanlar):
    def __init__(self,yasam_yeri,beslenme,tur,ayak_sayisi,ortalama_omur,ureme):
        super().__init__(yasam_yeri,beslenme,tur)
        self.ayak_sayisi = ayak_sayisi
        self.ortalama_omur = ortalama_omur
        self.ureme = ureme

    def bilgileri_goster(self):
        print("""
                Yaşam Yeri: {}
                Beslenme Şekli: {}
                Türü: {}
                Ayak Sayısı: {} adet
                Ortalama Ömrü: {} 
                Üreme Şekli: {}
                """.format(self.yasam_yeri, self.beslenme, self.tur, self.ayak_sayisi, self.ortalama_omur, self.ureme))

class Atlar(Hayvanlar):
    def __init__(self,yasam_yeri,beslenme,tur,ayak_sayisi,ortalama_omur,ureme):
        super().__init__(yasam_yeri,beslenme,tur)
        self.ayak_sayisi = ayak_sayisi
        self.ortalama_omur = ortalama_omur
        self.ureme = ureme

    def bilgileri_goster(self):
        print ("""
        Yaşam Yeri: {}
        Beslenme Şekli: {}
        Türü: {}
        Ayak Sayısı: {} adet
        Ortalama Ömrü: {} 
        Üreme Şekli: {}
        """.format(self.yasam_yeri,self.beslenme,self.tur,self.ayak_sayisi,self.ortalama_omur,self.ureme))

hayvan = Hayvanlar("Dünya","etçil,otçul,hepçil","hayvanlar alemi")
kus = Kuslar("Hava","etçil ve otçul","kuş",2,"5-10 yıl","Yumurtlama")
at = Atlar("Kara","Otçul","Memeli",4,"25-30 yıl","doğurarak")
kopek=Kopekler("Kara","Etçil","Memeli",4,"10-13 yıl","doğurarak")



print("""

Bilgilerini görmek istediğiniz hayvanı giriniz

1-Kuş
2-Köpek
3-At


""")


while True:

    islem=input("Seçiniz:")

    if(islem=='1'):

        print("Kuşlar sınıfı seçildi...")
        time.sleep(0.75)
        kus.bilgileri_goster()

    elif(islem=='2'):

        print("Köpekler seçildi...")
        time.sleep(0.75)
        kopek.bilgileri_goster()

    elif(islem=='3'):

        print("Atlar Seçildi...")
        time.sleep(0.75)
        at.bilgileri_goster()








