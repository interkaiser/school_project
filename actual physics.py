def posfinder(f, m, v0, x0, t):
    return str(x0+v0*t+f/m*t**2/2)


pos = int(input("Where you start: "))
vel = int(input("How fast you going: "))
frc = int(input("How strong da pull: "))
mas = int(input("How fat you are: "))
tim = int(input("How long you go: "))
print("You going to " + posfinder(frc,mas,vel,pos,tim))
