print('''
*************************************
Yazacağınız ilk sayı taban, ikinci sayı üs olacaktır.
*************************************
''')

a = int(input("sayı 1:"))
b = int(input("sayı 2:"))
c= a**b
toplam= 0

for i in str(c):
    i = int(i)
    toplam +=i
print("{} üzeri {} sayısının rakamları toplamı {}'dir".format(a,b,toplam))
