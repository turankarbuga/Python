
a=1
b=1
sayi=int(input("Kaç basamak bulmak istiyorsunuz?"))
fibonacci=[a,b]

for i in range(sayi-2):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)