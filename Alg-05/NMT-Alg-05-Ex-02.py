import time

def calcularTarifa(distancia):
    """
    Calcula o preço da tarifa de táxi, retornando o preço por KM percorrido acrescido da taxa mínima
    
    distancia = metros rodados
    """
    VALOR_INICIAL = 4
    VALOR_POR_KM = 0.25
    DISTANCIA_POR_TARIFA = 140
    return (VALOR_INICIAL + ((distancia / DISTANCIA_POR_TARIFA) * VALOR_POR_KM))

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():
    while True:                                                
        try:
            distancia = float(input("Informe a distância percorrida (metros): "))
            break
        except ValueError:
            mensagemErro()


    print("\n" * 130)
    print("Distância percorrida:", distancia)
    print("Preço da corrida: R$%.2f" % (calcularTarifa(distancia)))

if __name__ == "__main__":
    main()