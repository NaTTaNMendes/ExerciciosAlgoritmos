def calcularDivisores(numero):
    divisores = []
    
    for divisor in range(1, numero):
        if (numero % divisor == 0):
            divisores.append(divisor)
    
    return divisores

def isPerfeito(numero, numeros):
    soma = 0
    for item in numeros:
        soma += item
        
    if (soma == numero):
        return  True
    else:
        return False
    
def main():
    for numero in range(1, 10001):
        divisores = calcularDivisores(numero)
        if (isPerfeito(numero, divisores)):
            print(numero)

if __name__ == "__main__":
    main()