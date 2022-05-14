import time

def calcularFrete(quantidadeItens):
    """
    Retorna o valor do frete de uma quantidade x de itens, com o frete do primeiro item valendo mais que os demais
    
    quantidadeItens = int
    """
    PRIMEIRO_FRETE = 10.95
    DEMAIS_FRETES = 2.95
    return (PRIMEIRO_FRETE + ((quantidadeItens - 1) * DEMAIS_FRETES))

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():
    while True:                                                
        try:
            quantidade = int(input("Informe a quantidade de itens: "))
            break
        except ValueError:
            mensagemErro()

    print("\n" * 130)
    print("Quantidade de itens:", quantidade)
    print("Preço do frete: R$%.2f" % (calcularFrete(quantidade)))

if __name__ == "__main__":
    main()