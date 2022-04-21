import string

frase = input("Informe a frase: ").upper()
frase = frase.replace(" ", "")

a = 0                                               #Removendo acentos
punctuation = string.punctuation
while a < len(punctuation):
    frase = frase.replace(punctuation[a], "")
    a += 1

tamanho = len(frase)

a = 0
while a < tamanho:
    if (frase[a] != frase[tamanho - a - 1]):
        print("Não é um palíndromo")
        break
    a += 1
else:
    print("É um palíndromo")