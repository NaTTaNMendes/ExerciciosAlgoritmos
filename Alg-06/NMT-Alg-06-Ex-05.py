import time

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

numeros = []
while True:
    try:
        numero = input("Informe um número (vazio para sair): ")
        
        if (numero == ""):
            break
        
        numero = int(numero)
        numeros.append(numero)
    except:
        mensagemErro()
        
negativos = []
zeros = []
positivos = []
for numero in numeros:
    if (numero < 0):
        negativos.append(numero)
    elif (numero == 0):
        zeros.append(numero)
    else:
        positivos.append(numero)

for numero in negativos:
    print(numero)
for numero in zeros:
    print(numero)
for numero in positivos:
    print(numero)