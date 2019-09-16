print('''
You can find all numbers of  multiples of 3 or 5 and you can sum of this numbers with this code/ Bu kod ile 3 veya 5'in katı olan tüm sayıları bulabilir ve toplayabilirsiniz.
Which langue do you want? / Hangi dili istersiniz?
1-Turkish / Türkçe
2-English / İngilizce
''')
lang=int(input("Choose:"))
sum = 0
if(lang==2):
    print("Between two number [] and [] ")
    number1 = int(input("Number 1:"))
    number2= int(input("Number 2:"))

    for i in range(number1,number2):
        if(i%3== 0 or i % 5 == 0):
            print(i)
            sum += i
    print("Sum of this numbers is {}".format(sum))

elif(lang==1):
    print("[] ve [] arasında ")
    number1 = int(input("Sayı 1:"))
    number2 = int(input("Sayı 2:"))

    for i in range(number1, number2):
        if (i % 3 == 0 or i % 5 == 0):
            print(i)
            sum += i
    print("Bu sayıların toplamı {}".format(sum))
else:
    print("Please just type 1 or 2")
