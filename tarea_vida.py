tamaño = int(input("digite la longitud de la matriz:"))
matriz = [[["*"],["*"],["*"]],
          [["*"],["*"],["*"]],
          [["*"],["*"],["*"]]]

nueva = matriz
carril = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]#x, y

def generacion(x,y,cont):
    if x == len(matriz) and y == len(matriz) :

        return nueva
    else:
        nueva[x][y] = progreso(x, y, 0, 0, matriz[x][y])


def progreso(x,y,ind,tot,valor):

    if ind < 8:
        tot += existe_celula(matriz[(x + carril[ind][0]) % tamaño ][(y + carril[ind][1]) % tamaño])

        return progreso(x,y, ind + 1, tot, valor)
    else:
        return cuantos(valor,tot)

def existe_celula(x):
    if x == "-":
        return 0
    else:
        return 1

def cuantos(letra,tot):
    if letra == ["-"]:
        if tot == 3:
            return "*"
        else:
            return "-"
    elif letra == ["*"]:
        if tot == 2 or tot == 3:
            return ["*"]
        else:
            return ["-"]
    else:
        return ["p"]

print("d",generacion(0,0,0))
print(nueva[0])
print(nueva[1])
print(nueva[2])
