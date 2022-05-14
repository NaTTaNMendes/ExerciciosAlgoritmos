import time

def hex2int(hexa):
    """
    Converte um numero em hexadecimal positivo para inteiro. Retorna o inteiro convertido

    hexa = string
    """
    hexa = hexa.upper()
    tamanho = len(hexa)
    total = 0

    i = 0
    while (i < tamanho):
        if (hexa[i] == "A"):
            algarismo = 10
        elif (hexa[i] == "B"):
            algarismo = 11
        elif (hexa[i] == "C"):
            algarismo = 12
        elif (hexa[i] == "D"):
            algarismo = 13
        elif (hexa[i] == "E"):
            algarismo = 14
        elif (hexa[i] == "F"):
            algarismo = 15
        else:
            algarismo = int(hexa[i])

        total += algarismo * (16 ** (tamanho - i -1))
        i += 1
    
    return total

def int2hex(inteiro):
    """
    Converte um numero inteiro positivo para hexadecimal. Retorna a string convertida

    inteiro = int
    """
    saida = ""
    while True:
        resto = inteiro % 16
        inteiro = inteiro // 16
        if (resto == 10):
            saida = "A" + saida
        elif (resto == 11):
            saida = "B" + saida
        elif (resto == 12):
            saida = "C" + saida
        elif (resto == 13):
            saida = "D" + saida
        elif (resto == 14):
            saida = "E" + saida
        elif (resto == 15):
            saida = "F" + saida
        else:
            saida = str(resto) + saida
        if (inteiro < 16):
            if (inteiro == 10):
                saida = "A" + saida
            elif (inteiro == 11):
                saida = "B" + saida
            elif (inteiro == 12):
                saida = "C" + saida
            elif (inteiro == 13):
                saida = "D" + saida
            elif (inteiro == 14):
                saida = "E" + saida
            elif (inteiro == 15):
                saida = "F" + saida
            else:
                saida = str(inteiro) + saida
            break
    return saida

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
    while True:
        hexa = input("Informe um número em hexadecimal: ")
        if (hexa == ""):
            mensagemErro()
            continue
        hexa = hexa.upper()
        valido = True
        i = 0
        while i < len(hexa):
            try:
                vect = ["A", "B", "C", "D", "E", "F"]
                if (hexa[i] in vect):
                    i += 1
                    continue
                else:
                    int(hexa[i])
                    i += 1
            except ValueError:
                valido = False
                break
        if (valido):
            break
        else:
            mensagemErro()
    print("Número em decimal:", hex2int(hexa))

    print()
    inteiro = coletarInt("Informe um decimal: ")
    print("Número em hexadecimal:", int2hex(inteiro))

if __name__ == "__main__":
    main()
