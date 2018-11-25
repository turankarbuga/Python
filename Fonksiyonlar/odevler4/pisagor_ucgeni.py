
def pisagor():
    ucgen=[]

    for i in range(1,101):
        for j in range(1,101):

            c =((i**2) + (j**2)) ** (1/2)

            if (c==int(c)):
                ucgen.append((i,j,int(c)))
    return ucgen

for i in pisagor():
    print(i)