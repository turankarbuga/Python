a = 1
b = 1
fibonacci = [a,b]
while a+b < 4000000:
    a,b = b,a+b
    fibonacci.append(b)
list = list()
for i in fibonacci:
    if i%2 == 0:
        list.append(i)
sum = sum(list)
print(sum)