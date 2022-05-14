def mostrarOrdinal(numero):
    """
    Escreve o número ordinal do valor informado entre os valores 1 e 12, caso o valor esteja fora do escopo o retorno será nulo
    """
    if (numero == 1):
        return "Primeiro"
    elif (numero == 2):
        return "Segundo"
    elif (numero == 3):
        return "Terceiro"
    elif (numero == 4):
        return "Quarto"
    elif (numero == 5):
        return "Quinto"
    elif (numero == 6):
        return "Sexto"
    elif (numero == 7):
        return "Sétimo"
    elif (numero == 8):
        return "Oitavo"
    elif (numero == 9):
        return "Nono"
    elif (numero == 10):
        return "Décimo"
    elif (numero == 11):
        return "Décimo primeiro"
    elif (numero == 12):
        return "Décimo segundo"
    else:
        return ""

def main():
    for x in range(1, 13):
        print("%d - %s" % (x, mostrarOrdinal(x)))

if __name__ == "__main__":
    main()