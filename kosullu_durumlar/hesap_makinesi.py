
print("*****Calculator v1.0*****","\n")

number1=float(input("First Number:"))
number2=float(input("Second Number:"))
print("""

1-Addition
2-Substraction
3-Multiplication
4-Division

""")
operation=int(input("What would you like to do?:"))

if operation==1 :
    print("The sum of {} and {} is {}".format(number1,number2,number1+number2))
elif operation==2 :
    print("{} minus {} equals to{} ".format(number1,number2,number1-number2))
elif operation==3 :
    print("{} times {} is {} ".format(number1,number2,number1*number2))
elif operation==4 :
    print("{} divided by {} is {}".format(number1,number2,number1/number2))
else:
    print("Wrong operation number!")
