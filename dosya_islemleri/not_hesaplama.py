#update1 kalanları ve geçenleri ayıran kodlar eklendi. ayrı bir dosyaya yazılır. ödev1


def not_hesapla(satir):

    satir= satir[:-1]
    liste=satir.split(",")

    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    son_not=not1 * (3/10) + not2 * (3/10) + not3 * (2/5)
    liste2=[]
    liste2.append(son_not)
    for j in liste2:
        if(j>=60):
            file3=open("gecenler.txt","a",encoding="utf-8")
            file3.write(isim+"\n")
            file3.close()
        else:
            file4=open("kalanlar.txt","a",encoding="utf-8")
            file4.write(isim+"\n")
            file4.close()






    son_not=str(son_not)
    return isim + "--->" + son_not + "\n"




with open("dosya.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi=[]
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)













