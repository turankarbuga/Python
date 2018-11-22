birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

sayi=int(input("Sayı:"))

def yazılış(sayı):

    ilk_basamak=sayı%10
    ikinci_basamak=sayı//10

    return onlar[ikinci_basamak] +" "+birler[ilk_basamak]


print(yazılış(sayi))