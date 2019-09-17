from math import ceil

a = 600851475143
nums = list()
primes = list()

for i in range(2,ceil(600851475143 **0.5)):
    if a % i == 0:
        nums.append(i)


for prime_num in nums:
    count = 0
    for j in range(2, prime_num):
        if prime_num % j == 0:
            count += 1
            break
        else:
            pass
    if count == 0:
        primes.append(prime_num)

print(primes[-1])







