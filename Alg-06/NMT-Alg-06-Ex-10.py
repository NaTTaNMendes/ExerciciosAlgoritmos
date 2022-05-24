def adicionarConjuncao(palavras):
    """
    Retorna uma string contendo todas as palavras da lista informada agrupadas pelas regras de conjunção da Língua Portuguesa.


    palavras = lista(string)
    """
    if (len(palavras) == 1):
        return palavras[0]
    else:
        saida = ""
        for posicao in range(0, len(palavras)):
            if (posicao + 2 == len(palavras)):
                saida += palavras[posicao] + " e "
            else:
                if ((posicao + 1) == len(palavras)):
                    saida += palavras[posicao]
                else:
                    saida += palavras[posicao] + ", "
    
    return saida

def main():
    palavras = []
    while True:
        palavra = input("Informe um item da lista (vazio para parar): ")
        if (palavra == ""):
            break
        palavras.append(palavra)
    
    print("Itens formatados:", adicionarConjuncao(palavras))

if __name__=="__main__":
    main()