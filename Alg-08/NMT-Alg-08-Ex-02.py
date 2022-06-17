import time

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def coletarInt(texto):
    """
    Coleta qualquer número inteiro com tratamento de exceção. Retorna "" caso a entrada seja vazia.
    texto = enunciado da coleta
    """
    while True:
        try:
            numero = input(texto)
            if numero == "":
                break
            else:
                numero = int(numero)
            break
        except ValueError:
            mensagemErro()
    return numero

def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = coletarInt("Informe a posição do fibonacci: ")
    print("Número na posição %.0f: %.0f" % (n, fibonacci(n)))

if __name__=="__main__":
    main()