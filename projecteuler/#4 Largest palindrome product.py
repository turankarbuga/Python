numbers = list()
palindrom = list()
for i in range(100,1000):
    for j in range(100,1000):
        numbers.append(i * j)

for i in numbers:
    i = str(i)
    if i == i[::-1]:
        i = int(i)
        palindrom.append(i)

palindrom.sort()
print(palindrom[-1])

