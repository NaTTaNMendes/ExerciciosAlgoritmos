def isInteger(texto):
    """
    Retorna se o conteúdo de um texto é um inteiro válido

    texto = string
    """
    texto = texto.strip()

    for i in range(0, len(texto)):
        if (i == 0):
            if (texto[i] == "+" or texto[i] == "-"):
                continue
        try:
            int(texto[i])
        except ValueError:
            return False
  
    return True

def main():
    texto = input("Informe um número: ")
    if (isInteger(texto)):
        print("É um inteiro válido")
    else:
        print("Não é um inteiro válido")

if __name__ == "__main__":
    main()