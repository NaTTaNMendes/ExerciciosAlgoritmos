import time

def mensagemErro():                                             
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

numeros = []
while True:
    try:
        numero = int(input("Informe um número (0 para sair): "))
        
        if (numero == 0):
            break
        else:
            numeros.append(numero)
            
    except:
        mensagemErro()

print("\n" * 130)
print("Lista informada:", numeros)

numeros.sort(reverse = True)
print("Lista decrescente:")
for numero in numeros:
    print(numero)
