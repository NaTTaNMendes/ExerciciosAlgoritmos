from math import sqrt

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if (a == 0):
    print("Valor inválido")
else:
    discriminante = (b ** 2) - ((4 * a) * c)
    if (discriminante < 0):
        print("Quantidade de raízes: 0")
    elif(discriminante == 0):
        raiz = (-b) / (2 * a)
        print("Quantidade de raízes: 1")
        print("Raíz: ", raiz)
    else:
        raiz1 = (-b + sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - sqrt(discriminante)) / (2 * a)
        print("Quantidade de raízes: 2")
        print("Primeira raíz: ", raiz1)
        print("Segunda raíz: ", raiz2)    