import time

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

def calcularDivisores(numero):
    divisores = []
    
    for divisor in range(1, (numero + 1)):
        if (numero % divisor == 0):
            divisores.append(divisor)
    
    return divisores
    
def main():
    while True:
        numero = coletarInt("Informe um número: ")
        if (numero < 0):
            mensagemErro()
        else:
            break
    
    print("Divisores de", numero,":",calcularDivisores(numero))

if __name__ == "__main__":
    main()