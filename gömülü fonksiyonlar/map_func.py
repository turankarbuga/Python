liste=[(3,4),(10,3),(5,6),(1,9)]

def carpma(sayilar):
    return sayilar[0] * sayilar[1]
liste2=list(map(carpma,liste))
print(liste2)
