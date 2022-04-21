from math import sqrt

x = float(input("Digite a coordenada x de um ponto: "))
y = float(input("Digite a coordenada y de um ponto: "))

x1 = x
y1 = y

perimetro = 0

while True:    
    teste = input("Digite a coordenada x de um ponto (enter para sair): ")
    if (teste == ""):
        d = sqrt((abs(y2 - y) ** 2) + (abs(x2 - x) ** 2))
        perimetro = perimetro + d
        break
    x2 = float(teste)
    y2 = float(input("Digite a coordenada y de um ponto: "))

    d = sqrt((abs(y2 - y1) ** 2) + (abs(x2 - x1) ** 2))
    perimetro = perimetro + d

    y1 = y2
    x1 = x2
print("O perímetro deste polígono é igual a", perimetro)