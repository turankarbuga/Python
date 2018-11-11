limit = int(input("Put the Limit (1000 for project Euler):"))
list1=[]


for i in range(1,limit+1):
    list1.append(i**i)

sum=sum(list1)
sum=str(sum)
list2=list(sum)


print(list2[-10:])
