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

    """PRECISO CORRIGIR O ERRO DOS OPERADORES UNARIO NA OPERACAO AQUI REALIZADA"""
    while True:
        if (expressao[0] in operadoresBinarios): 
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