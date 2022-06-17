import time

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def conversorBinarioRecursivo(q):
    if q == 0:
        return ""
    return conversorBinarioRecursivo(q // 2) + str(q % 2)

def main():
    while True:
        q = int(input("Informe um inteiro positivo: "))
        if (q < 0):
            mensagemErro()
        else:
            break
    print("Valor em decimal: %.0f \nValor em binário: %s" % (q, conversorBinarioRecursivo(q)))

if __name__=="__main__":
    main()