def mukemmel_sayi(func):

    def wrapper():
        print("Mükemmel Sayılar")
        for sayi in range(1, 1001):
            bolenler = list()

            for i in range(1, sayi):
                if (sayi % i == 0):
                    bolenler.append(i)
                    if (sum(bolenler) == sayi):
                        print(sayi)
        func()
    return wrapper



@mukemmel_sayi
def asal_sayi():
    print("----------------")
    print("Asal Sayılar")
    for sayi in range(2,1001):

        i = 2
        sayac = 0

        while(i<sayi):
            if(sayi%i==0):
                sayac +=1
            i +=1
        if(sayac == 0):
            print(sayi)

asal_sayi()


