palavras = []
while True:
    palavra = input("Informe uma palavra (vazio para sair): ")
    if (palavra == ""):
        break
    if (not(palavra in palavras)):
        palavras.append(palavra)

for palavra in palavras:
    print(palavra)