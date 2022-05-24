from random import randint

def geradorLoteria():
    """
    Retorna um bilhete de loteria com 6 números entre 1 e 60 ordenados de forma crescente, não terão valores repetidos.
    """
    numeros = []   
    while True:
        valor = randint(1, 60)
        if not(valor in numeros):
            numeros.append(valor)
        if (len(numeros) == 6):
            break
    
    numeros.sort()
    return numeros

def main():
    print("Números gerados:",geradorLoteria())

if __name__=="__main__":
    main()
