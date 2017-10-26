def multi(a):
    if(a == 0):
        return 1
    else:
        return a*multi(a - 1)


print(multi(int(input("Factorial to calculate: "))))
