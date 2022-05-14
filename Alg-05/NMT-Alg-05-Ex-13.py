import time

def verDiasNoMes(ano, mes):
    """
    Retorna a quantidade de dias na data informada.

    ano = int

    mes = int
    """
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return 31
    else:
        if ((ano % 400 == 0 or ano % 4 == 0) and mes == 2):
            return 29
        if (mes == 2):
            return 28
        return 30

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
    ano = coletarInt("Informe o ano: ")
    while True:
        mes = coletarInt("Informe o mês: ")
        if (mes < 1 or mes > 12):
            mensagemErro()
        else:
            break
    print("Quantidade de dias no mês:", verDiasNoMes(ano, mes))

if __name__ == "__main__":
    main()
