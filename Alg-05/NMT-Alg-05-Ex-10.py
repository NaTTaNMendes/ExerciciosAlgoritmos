import time

def isPrime(numero):
    """
    Informa se um inteiro é primo ou não

    numero = int
    """
    for i in range (2, numero):
        if (numero % i == 0):
            return False
    return True

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def coletarInt(texto):
    """
    Coleta qualquer número inteiro com tratamento de exceção

    texto = enunciado da coleta
    """
    while True:
        try:
            numero = int(input(texto))
            break
        except ValueError:
            mensagemErro()
    return numero

def main():
    numero = coletarInt("informe um inteiro: ")
    if (isPrime(numero)):
        print("O número é primo")
    else: 
        print("O número não é primo")

if __name__ == "__main__":
    main()