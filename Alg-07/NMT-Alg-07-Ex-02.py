import time

def diferencaSimetrica(conjunto1, conjunto2):
    """
    Retorna um conjunto com a diferenca simetrica entre os dois conjuntos informados.


    conjunto 1 = set


    conjunto 2 = set
    """ 
    saida = list(conjunto1.difference(conjunto2))
    saida.extend(list(conjunto2.difference(conjunto1)))
    saida.sort()
    return saida

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

def main():
    A = set()
    B = set()

    while True:
        numero = coletarInt("Informe os números do primeiro conjunto (enter para sair): ")
        if numero == "":
            break
        A.add(numero)

    while True:
        numero = coletarInt("Informe os números do segundo conjunto (enter para sair): ")
        if numero == "":
            break
        B.add(numero)
    
    diferenca = diferencaSimetrica(A,B)
    print("Diferença simétrica:", diferenca)

if __name__=="__main__":
    main()