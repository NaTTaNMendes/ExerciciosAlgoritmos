def calcularTotal():
    numero = input("Informe um numero: ")
    if (numero == ""):
        return 0     
    return float(numero) + calcularTotal()

print(calcularTotal())  