import time

def converterBaseParaInteiro(numero, base):
    """
    Converte um numero em qualquer base entre 2 e 16 positivo para decimal. Retorna o inteiro convertido

    numero = string

    base = int
    """
    numero = numero.upper()
    tamanho = len(numero)
    total = 0

    i = 0
    while (i < tamanho):
        if (numero[i] == "A"):
            algarismo = 10
        elif (numero[i] == "B"):
            algarismo = 11
        elif (numero[i] == "C"):
            algarismo = 12
        elif (numero[i] == "D"):
            algarismo = 13
        elif (numero[i] == "E"):
            algarismo = 14
        elif (numero[i] == "F"):
            algarismo = 15
        else:
            algarismo = int(numero[i])

        total += algarismo * (base ** (tamanho - i -1))
        i += 1
    
    return total

def converterInteiroParaBase(numero, base):
    """
    Converte um numero inteiro positivo em qualquer base entre 2 e 16. Retorna a string convertida

    numero = int

    base = int
    """
    saida = ""
    while True:
        resto = numero % base
        numero = numero // base
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
        if (numero < base):
            if (numero == 10):
                saida = "A" + saida
            elif (numero == 11):
                saida = "B" + saida
            elif (numero == 12):
                saida = "C" + saida
            elif (numero == 13):
                saida = "D" + saida
            elif (numero == 14):
                saida = "E" + saida
            elif (numero == 15):
                saida = "F" + saida
            else:
                saida = str(numero) + saida
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
        print("Conversões disponíveis:")
        print()
        print("2 - binário               7 - heptal               12 - duodecimal")
        print("3 - ternário              8 - octal                13 - tridecimal")
        print("4 - quarternário          9 - nonal                14 - tetradecimal")
        print("5 - quintal              10 - decimal              15 - pentadecimal")
        print("6 - sextal               11 - undecimal            16 - hexadecimal")
        print()
        base = input("Base para conversão: ")

        if (base == ""):
            continue

        try:
            base = int(base)
            if (base < 2 or base > 16):
                mensagemErro()
                continue
        except ValueError:
            mensagemErro()
            continue
        print("\n" * 130)
        break

    while True:
        print("1 - Conveter de base 10 para base %d" % base)
        print("2 - Converter de base %d para base 10" % base)
        print()
        escolha = input("Escolha uma opção: ")

        if (escolha == ""):
            mensagemErro()
            continue

        try:
            escolha = int(escolha)
            if (escolha < 1 or escolha > 2):
                mensagemErro()
                continue
        except ValueError:
            mensagemErro()
            continue
        print("\n" * 130)
        break
    
    if (escolha == 1):  
        numero = coletarInt("Informe o número a ser convertido para a base %d: " % base)
        print("\n" * 130)
        print("Número na base %d: %s" % (base, converterInteiroParaBase(numero, base)))
    else:
        while True:
            numero = input("Informe um número na base %d: " % base)
            if (numero == ""):
                mensagemErro()
                continue
            numero = numero.upper()
            valido = True
            vect = "ABCDEF"
            for letra in numero:
                try:
                    int(letra)
                except:
                    if (base > 10):
                        casas = base - 10
                    for posicao in range(casas):
                        if (letra == vect[posicao]):
                            valido = True
                            break
                        else:
                            valido = False                
            if (valido):
                break
            else:
                mensagemErro()
        print("Número em decimal:", converterBaseParaInteiro(numero, base))
    
if __name__ == "__main__":
    main()