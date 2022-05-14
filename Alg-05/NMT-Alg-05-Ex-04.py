import time

def calcularMediana(valores):
    """
    Recebe uma lista de valores inteiros e retorna a mediana
    
    valores = lista de inteiros
    """
    valores.sort()
    if (len(valores) % 2 == 1):
        return valores[(len(valores) % 2) + 1]
    else:
        return valores[(len(valores) // 2) - 1], valores[(len(valores) // 2)]

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():
    vetor = []
    while True:                                                     
        try:
            numero = input("Informe um valor para o vetor (Enter para parar): ")
            if (numero == ""):
                break
            numero = float(numero)
            vetor.append(numero)
        except ValueError:
            mensagemErro()

    print("\n" * 130)
    print("Valores informados:", vetor)
    print("Mediana(s):", calcularMediana(vetor))

if __name__ == "__main__":
    main()