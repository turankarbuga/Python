
s = ""
liste = list()
with open("odev1.txt","r",encoding="utf-8") as file:

    for i in file:
        for harfler in i:
            liste.append(harfler)
            break

for i in liste:

    s += i

print(s)




