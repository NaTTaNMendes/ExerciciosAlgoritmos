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

def fatorial(n):
    if (n == 0):
        return 1
    return (n * fatorial(n-1))

def main():
    numero = coletarInt("Informe o inteiro para calcular o fatorial: ")
    print("Fatorial:", fatorial(numero))

if __name__=="__main__":
    main()