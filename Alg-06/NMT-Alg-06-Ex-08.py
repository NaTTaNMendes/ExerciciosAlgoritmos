def somentePalavras(texto):
    """
    Recebe um texto e o divide em várias palavras dentro de uma lista, os espaços e símbolos de pontuação são removidos.
    Retorna uma lista de strings
    

    texto = string
    """
    texto.strip()
    palavras = []
    acentos = [",",".",";","!","?"," ",":"]
    inicio = 0
    for posicao in range(0, len(texto)):
        if (texto[posicao] in acentos):
            if (texto[posicao - 1] in acentos):
                inicio += 1
            else:
                palavras.append(texto[inicio:posicao])
                inicio = posicao + 1
    return palavras

def main():
    texto = input("Informe um texto com acentos: ")
    saida = somentePalavras(texto)
    for palavra in saida:
        print(palavra)

if __name__=="__main__":
    main()