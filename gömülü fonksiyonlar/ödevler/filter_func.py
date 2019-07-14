liste=[(3,4,5),(6,8,10),(3,10,7)]

def ucgen(sayilar):

    if(sayilar[0]+sayilar[2]>sayilar[1] and abs(sayilar[0])-sayilar[2]<sayilar[1]):
        return True
    else:
        return False


print(list(filter(ucgen,liste)))