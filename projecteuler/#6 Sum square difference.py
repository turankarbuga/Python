squaresSum = 0
sumSquares = 0

for i in range(1,101):
    squaresSum += i**2

for i in range(1,101):
    sumSquares += i

print(sumSquares**2-squaresSum)