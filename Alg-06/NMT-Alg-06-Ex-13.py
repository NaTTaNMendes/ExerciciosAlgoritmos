import time

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def countRange(lista, minimo, maximo):
    """
    Retorna a quantidade de valores entre o mínimo e o máximo informados.

    lista = lista(float)

    minimo = float

    maximo = float
    """
    quantidade = 0
    for item in lista:
        if (item >= minimo and item <= maximo):
            quantidade += 1

    return quantidade 

def coletarFloat(texto):
    """
    Coleta qualquer número float com tratamento de exceção
    texto = enunciado da coleta
    """
    while True:
        try:
            numero = float(input(texto))
            break
        except ValueError:
            mensagemErro()
    return numero

def main():
    numeros = []
    while True:
        numero = input("Informe um número (vazio para sair): ")
        if (numero == ""):
            break
        try:
            numeros.append(float(numero))
        except ValueError:
            mensagemErro()

    minimo = coletarFloat("Informe o valor mínimo: ")
    maximo = coletarFloat("Informe o valor máximo: ")

    print("Quantidade de valores entre o mínimo e o máximo:", countRange(numeros, minimo, maximo))

if __name__=="__main__":
    main()