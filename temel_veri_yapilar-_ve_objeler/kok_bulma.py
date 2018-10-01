print("kök bul")


a = int(input("ikinci dereceden denklemin baş katsayısını giriniz:"))
b= int(input("x'in katsayısını giriniz:"))
c= int(input("sabit sayıyı giriniz:"))
delta= b**2 - 4*a*c

x1= (-b + (delta)** 0.5 )/2*a
x2 = (-b - (delta)** 0.5 )/2*a

print("ikinci dereceden denkleminizin kökleri {} ve {}".format(x1,x2))