def tokenizar(expressao):
    """
    Divide os elementos da expressão em tokens e retorna uma lista com todos eles (A função não consegue detectar números negativos).


    expressao = string
    """
    tokens = []
    expressao = expressao.replace(" ", "")
    operadores = ["+", "-", "*", "/", "^"]

    while True:
        if (expressao[0] == "("):
            for simbolo in expressao:
                if (simbolo == ")"):
                    try:
                        tokens.append(expressao[0 : expressao.index(")") + 1])
                        expressao = expressao[expressao.index(")") + 1 ::]
                        break
                    except:
                        tokens.append(expressao[0 ::])
                        expressao = ""
                        break
            if (expressao == ""):
                break

        elif (expressao[0] in operadores):
            tokens.append(expressao[0])
            expressao = expressao[1 ::]

        else:
            acabou = True
            for i in range(0, len(expressao)):
                if (expressao[i] in operadores):
                    tokens.append(expressao[0 : i])
                    expressao = expressao[i ::]
                    acabou = False
                    break
            if (acabou):
                tokens.append(expressao[0 ::])
                break

    return tokens

def main():
    expressao = input("Informe uma expressão matemática: ")
    tokens = tokenizar(expressao)
    print("Tokens na expressão:", tokens)

if __name__=="__main__":
    main()