
"""
denklem formatı (ax+b=c)
3x+5=14
4x-1=19
7x+4=11

"""

a= int(input("x'in kat sayısı:"))
b= int(input("sabit sayı:"))
c= int(input("denklem kaça eşit?:"))

x = (c - b) / a
print("birinci dereceden denkleminizin kökü {}".format(x))


