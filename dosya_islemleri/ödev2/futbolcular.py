
def futbolculari_ayir(satir):

    satir=satir[:-1]
    liste=satir.split(",")
    isim=liste[0]


    for j in liste:
        if(j=="Beşiktaş"):
            with open("bjk.txt","a",encoding="utf-8") as file2:
                file2.write(isim+"\n")
        elif(j=="Fenerbahçe"):
            with open("fb.txt","a",encoding="utf-8") as file3:
                file3.write(isim+"\n")
        elif(j=="Galatasaray"):
            with open("gs.txt","a",encoding="utf-8") as file4:
                file4.write(isim+"\n")


with open("futbolcular.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi=[]
    for i in file:
        eklenecekler_listesi.append(futbolculari_ayir(i))