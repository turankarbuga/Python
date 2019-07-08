import time

class Bilgisayar():

    def __init__(self,islemci,ram,ekran_karti,sistem,klavye,batarya_omru,depolama,marka,model,fiyat):
        self.islemci=islemci
        self.ram=ram
        self.ekran_karti=ekran_karti
        self.sistem=sistem
        self.klavye=klavye
        self.batarya_omru=batarya_omru
        self.depolama=depolama
        self.marka=marka
        self.model=model
        self.fiyat=fiyat

    def bilgileri_goster(self):

        print("""
        
        İşlemci: {}
        Ram: {}
        Ekran Kartı: {}
        Sistem: {}
        Klavye: {}
        Batarya Ömrü: {}
        Depolama: {}
        Marka: {}
        Model: {}
        Fiyat: {}
        
        """.format(self.islemci,self.ram,self.ekran_karti,self.sistem,self.klavye,self.batarya_omru,self.depolama,self.marka,self.model,self.fiyat))

bilgisayar = Bilgisayar("İntel Core i5-9300H","8GB","Nvidia GTX 1650","FreeDOS","4 Bölge RGB aydınlatma","4-6 saat","480GB SSD","Monster","Abra A5 v15.1.1",5800)

bilgisayar.bilgileri_goster()






