posicao = input("Informe a posição: ")
posicao = posicao.upper()

numero = int(posicao[1])

if(posicao[0] == 'A' or posicao[0] == 'C' or posicao[0] == 'E' or posicao[0] == 'G'):
    if (numero % 2 == 1):
        print("PRETO")
    else:
        print("BRANCO")
else:
    if (numero % 2 == 0):
        print("PRETO")
    else:
        print("BRANCO")