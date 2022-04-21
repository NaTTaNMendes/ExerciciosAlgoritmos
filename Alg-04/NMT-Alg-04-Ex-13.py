numero = int(input("Digite um número inteiro (maior ou igual a 2): "))

i = 2
while i <=9:
    if (numero % i == 0):
        while (numero % i == 0):
            print(i)
            numero = numero / i
    i += 1
else:
    if (numero != 1):
        print(numero)