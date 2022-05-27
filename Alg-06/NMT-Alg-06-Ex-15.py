from cmath import exp


def tokenizar(expressao):
    """
    Divide os elementos da expressão em tokens e retorna uma lista com todos eles (A função não consegue detectar números negativos).


    expressao = string
    """
    tokens = []
    expressao = expressao.replace(" ", "")
    operadoresBinarios = ["+", "-", "*", "/", "^", ")", "("]
    operadoresUnarios = ["+", "-"]
    pos = 0

    while True:
        if (expressao[0] in operadoresUnarios):
            if (len(tokens) == 0):
                for i in range(1, len(expressao)):
                    if (expressao[i] in operadoresBinarios):
                        tokens.append(expressao[0 : i])
                        expressao = expressao[i :: ]
                        break
                break 
            elif (("-" in tokens[pos - 1]) and (len(tokens[pos - 1]) == 1)) or (("+" in tokens[pos - 1]) and (len(tokens[pos - 1]) == 1)) or (")" in tokens[pos - 1]):
                tokens.append(expressao[0])
                expressao = expressao[1 ::]
            else:
                for i in range(1, len(expressao)):
                    if (expressao[i] in operadoresBinarios) or (expressao[i] == "(") or (expressao[i] == ")"):
                        tokens.append(expressao[0 : i])
                        expressao = expressao[i ::]
                        break    

        elif (expressao[0] in operadoresBinarios):
            tokens.append(expressao[0])
            expressao = expressao[1 ::]

        else:
            acabou = True
            for i in range(0, len(expressao)):
                if (expressao[i] in operadoresBinarios):
                    tokens.append(expressao[0 : i])
                    expressao = expressao[i ::]
                    acabou = False
                    break
            if (acabou):
                tokens.append(expressao[0 ::])
                break

        pos = pos + 1

    return tokens

def main():
    expressao = input("Informe uma expressão matemática: ")
    tokens = tokenizar(expressao)
    print("Tokens na expressão:", tokens)

if __name__=="__main__":
    main()