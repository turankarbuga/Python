
for a in range(1,500):
    for b in range(1,500):
        c = (a**2 + b**2)**0.5
        if (a+b+c == 1000) and (a < b < c):
            print("a: {}\nb: {}\nc: {}".format(a,b,int(c)))
            print("the answer:",int(a*b*c))
