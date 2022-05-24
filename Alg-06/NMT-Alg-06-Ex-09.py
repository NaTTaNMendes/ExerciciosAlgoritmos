import time

def mensagemErro():
    """ Informa uma mensagem de erro para o usuário e limpa a tela"""                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def coletarFloat(texto):
    """
    Coleta qualquer número float com tratamento de exceção

    texto = enunciado da coleta
    """
    while True:
        try:
            numero = float(input(texto))
            break
        except ValueError:
            mensagemErro()
    return numero

def main():
    numeros = []
    while True:
        numero = input("Informe um número (vazio para sair): ")
        if (numero == ""):
            break
        try:
            numeros.append(float(numero))
        except ValueError:
            mensagemErro()
    
    total = 0
    for numero in numeros:
        total += numero

    media = total / len(numeros)

    print("Média:", media)

    temMenor = False
    for numero in numeros:
        if (numero < media):
            if (temMenor == False):      
                print("Menores que a média")
                temMenor = True
            print(numero)

    if (media in numeros):
        print()        
        print("Iguais a média")
        for numero in numeros:
            if (numero == media):
                print(numero)

    temMaior = False
    for numero in numeros:
        if (numero > media):
            if (temMaior == False):
                print()
                print("Maiores que a média")
                temMaior = True
            print(numero)


if __name__=="__main__":
    main() 