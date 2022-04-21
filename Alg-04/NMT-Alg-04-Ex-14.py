numero = input("Informe o binário: ")

tamanho = len(numero)
total = 0

i = 0
while (i < tamanho):
    total += int(numero[i]) * (2 ** (tamanho - i -1))
    i += 1

print(total)