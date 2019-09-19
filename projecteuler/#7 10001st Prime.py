i = 1
primes = list()

while len(primes) < 10001:
    count = 0
    i += 1
    for j in range(2,i):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        primes.append(i)

print(primes[-1])