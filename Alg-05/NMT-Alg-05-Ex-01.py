from math import sqrt
import time

def calcularHipotenusa(cateto1, cateto2):
    """
    Coleta dois catetos e retorna a hipotenusa de um triângulo retângulo
    
    cateto 1 - Float
    
    cateto 2 - Float
    """
    return sqrt((cateto1 ** 2) + (cateto2 ** 2))

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():
    while True:                                                
        try:
            cateto1 = float(input("Informe o primeiro cateto: "))
            break
        except ValueError:
            mensagemErro()

    while True:                                                
        try:
            cateto2 = float(input("Informe o segundo cateto: "))
            break
        except ValueError:
            mensagemErro()
    
    print("\n" * 130)
    print("Tamanho do primeiro cateto:", cateto1)
    print("Tamanho do segundo cateto:", cateto2)
    print("Tamanho da hipotenusa:", calcularHipotenusa(cateto1, cateto2))

if __name__ == "__main__":
    main()