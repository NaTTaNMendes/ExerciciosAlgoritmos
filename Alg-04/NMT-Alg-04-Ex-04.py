#FALTA CORREÇÃO

from math import sqrt

x = float(input("Digite a coordenada x de um ponto: "))
y = float(input("Digite a coordenada y de um ponto: "))

perimetro = 0

while True:    
    x1 = input("Digite a coordenada x de um ponto (enter para sair): ")
    if (x1 == ""):
        break
    x1 = float(x1)
    y1 = float(input("Digite a coordenada y de um ponto: "))

    d = sqrt((abs(y1 - y) ** 2) + (abs(x1 - x) ** 2))
    perimetro = perimetro + d

    x = x1
    y = y1

print("O perímetro deste polígono é igual a", perimetro)