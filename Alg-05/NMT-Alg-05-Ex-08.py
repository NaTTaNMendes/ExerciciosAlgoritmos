def corrigirMaiuscula(texto):
    """
    Corrige as maiúsculas de uma string, se adequando as regras da língua portuguesa. Retorna o texto corrigido

    texto = string
    """
    texto = texto.lower()
    texto = texto.strip()
    saida = ""
    elevarProximo = False
    for i in range(0, len(texto)):
        try:
            if (texto[i - 1] == "." or texto[i - 1] == "!" or texto[i - 1] == "?" or i == 0):
                saida += texto[i].upper()
                if (texto[i] == " "):
                    elevarProximo = True                
            else:
                if (elevarProximo):
                    saida += texto[i].upper()
                    elevarProximo = False
                else:
                    saida += texto[i]
        except IndexError:
            saida += texto[i]
    return saida

def main():
    texto = input("Informe um texto: ")
    print("\n" * 130)
    print("Texto informado:", texto)
    print("Texto formatado:", corrigirMaiuscula(texto))

if __name__ == "__main__":
    main()