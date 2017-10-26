def pythonagoras(a, b, c):
    return str((a**2+b**2+c**2)**(1/2))


len = int(input())
wid = int(input())
hit = int(input())
print(pythonagoras(len,wid,hit))
