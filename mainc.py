from random import randint
lista = [ "joseph", "ruben", "yo", "rvenegas", "felipa"]
def grupos():
    grupo1 = []
    grupo2 = []

    for x in lista:
        if randint(0,1) == 1:
            if len(grupo1) == 2:
                grupo2.append(x)
            else:
                grupo1.append(x)
        else:
            if len(grupo1) == 2:
                grupo2.append(x)
            else:
                grupo1.append(x)

    print("grupo1: ", grupo1)
    print("grupo2: ", grupo2)

grupos()
