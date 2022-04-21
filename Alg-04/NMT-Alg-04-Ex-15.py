numero = int(input("informe o número: "))

r = 0
saida = ""

while (numero != 0):
    r = numero % 2
    saida = str(r) + saida
    numero = int(numero / 2)

print(saida)