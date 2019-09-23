from math import ceil
sum = 2
for i in range(2,2000000):
    count = 0
    for j in range(2,ceil(i**0.5)+1):
        if i % j == 0:
            count += 1
            break

    if count == 0:
        sum += i
print(sum)
