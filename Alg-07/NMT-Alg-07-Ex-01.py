def isCaracterUnico (string):
    """
    Verifica se todos os caracteres da string são únicos. Retornando True caso verdadeiro.


    string = string
    """
    string = string.replace(" ", "")
    conjunto = set(string)
    if (len(conjunto) == len(string)):
        return True
    else:
        return False

def main():
    string = input("Infome um texto: ")
    if (isCaracterUnico(string)):
        print("O texto não possui caracteres repetidos")
    else:
        print("O texto possui caracteres repetidos")

if __name__=="__main__":
    main()