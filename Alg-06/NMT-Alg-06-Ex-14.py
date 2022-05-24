import time

def precedencia(operador):
    """
    Retorna a ordem de precedencia do operador informado. 1 para '+' ou '-', 2 para '*' ou '/' e 3 para '^'. Caso não seja nenhum desse será retornado -1.


    operador = string
    """
    if (operador == "+" or operador == "-"):
        return 1
    elif (operador == "*" or operador == "/"):
        return 2
    elif (operador == "^"):
        return 3
    else:
        return -1

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():
    while True:
        operador = input("Informe um operador: ")
        if (len(operador) > 1):
            mensagemErro()
        else:
            break

    Valorprecedencia = precedencia(operador)
    if (Valorprecedencia == -1):
        print("O operador não existe")
    else:
        print("Precedência do operador:", Valorprecedencia)

if __name__=="__main__":
    main()