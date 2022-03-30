valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)
meio = (valor1 + valor2+ valor3) - maior - menor

print("Maior:",maior,"\nMeio:",meio,"\nMenor:",menor)