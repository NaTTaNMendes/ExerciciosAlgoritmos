valor = float(input("Insira o valor: "))

if (valor == 4):
    print("Raíz: %.12f" % 4)
else:
    a = 2
    while abs(valor - (a ** 2)) > (10 ** -12):
        raiz = (a + (valor / a)) / 2
        a = raiz   
    print("Raíz: %.12f" % raiz)