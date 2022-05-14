import time

def validarTriangulo(lado1, lado2, lado3):
    """
    Recebe os três lados de um triângulo e retorna se ele é válido ou não

    lado1 = float

    lado2 = float

    lado3 = float
    """
    if (lado1 >= (lado2 + lado3)):
        return False
    elif (lado2 >= (lado1 + lado3)):
        return False
    elif (lado3 >= (lado2 + lado1)):
        return False
    return True

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def coletarFloat(texto):
    """
    Coleta qualquer número real com tratamento de exceção

    texto = enunciado da coleta
    """
    while True:
        try:
            lado = float(input(texto))
            break
        except ValueError:
            mensagemErro()
    return lado

def main():
    lado1 = coletarFloat("Informe o primeiro lado: ")
    lado2 = coletarFloat("Informe o segundo lado: ")
    lado3 = coletarFloat("Informe o terceiro lado: ")

    teste = validarTriangulo(lado1, lado2, lado3)

    if (teste):
        print("O triângulo é válido")
    else:
        print("O triângulo não é válido")
        
if __name__ == "__main__":
    main()