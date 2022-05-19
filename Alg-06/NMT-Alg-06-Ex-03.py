import time

def removendoExtremos(numeros, limite):
    if (limite > len(numeros)):
        print("Erro: A lista é menor que o número informado")
        return
    else:
        temp = numeros
        temp.sort()
        menores = temp[:limite]
        maiores = temp[-1:-(limite + 1):-1]
        return (menores, maiores)

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
 
limite = coletarInt("Informe um número para a comparação: ")
saida = removendoExtremos(numeros,limite)

print("Lista original:", numeros)
print(limite,"menores elementos:",saida[0])
print(limite,"maiores elementos:",saida[1])
