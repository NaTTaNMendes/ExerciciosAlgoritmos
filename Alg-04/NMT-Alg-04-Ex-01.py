numero = int(input("Informe um número (0 sai do loop): "))

ValorTotal = 0
total = 0

if (numero != 0):
    while True:
        ValorTotal += numero
        total += 1
        numero = int(input("Informe um número (0 sai do loop): "))
        if (numero == 0):
            break
    print("Média: ", ValorTotal/total)
else:
    print("SAIU DO LOOP")

