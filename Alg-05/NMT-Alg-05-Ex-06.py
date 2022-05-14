import time

def centralizarString(string, largura):
    """
    Retorna a string centralizada pela largura de caracteres disponíveis em cada linha do terminal

    string = string

    largura = int
    """
    qtdEspacos = largura - len(string)
    saida = ""
    for x in range(1, qtdEspacos // 2):
        saida += " "
    saida += string
    return saida

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def main():

    print("Encontre a largura do seu terminal")
    print("Quando a quantidade de '1's  cobrir corretamente uma linha pressione y")
    print()
    input("Pressione enter para continuar")

    largura = 0
    b = 100
    while True:
        a = 0
        for x in range(1, b):
            print("1", end = "")
            a += 1
        print()
        print("Largura padrão:", b)
        continuar = input("O valor está correto? (y se sim): ")
        continuar = continuar.upper()
        if (continuar == "Y"):
            largura = a
            break
        else:
            while True:
                try:
                    numero = int(input("Informe a largura do terminal: "))
                    b = numero
                    break
                except ValueError:
                    mensagemErro()
        print("\n" * 130)

    texto = input("Informe o texto para ser centralizado: ")
    print("\n" * 130)
    print("Texto informado:", texto)
    print()
    print("Texto cetralizado:")
    print(centralizarString(texto, largura))

if __name__ == "__main__":
    main()