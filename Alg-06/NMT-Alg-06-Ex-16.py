from inspect import stack

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

def precedencia(operador):
    """
    Retorna a ordem de precedencia do operador informado. 1 para '+' ou '-', 2 para '*' ou '/' e 3 para '^'. Caso não seja nenhum desse será retornado -1.
    operador = string
    """
    if (operador == "+" or operador == "-"):
        return 1
    elif (operador == "*" or operador == "/"):
        return 2
    elif (operador == "^"):
        return 3
    else:
        return -1

def infixToPosFix(tokens):
    '''Esse método transforma uma lista de tokens infixa para uma nova pósfixa.


    tokens = lista de tokens da expressao
    '''
    saida = []
    operador = stack()

    operadores = ["+","-","/","*"]

    for token in tokens:
        if isInteger(token):
            saida.append(token)
        elif token == "(":
            operador.push(token)
        elif token == ")":
            tokenAcima = operador.pop()
            while tokenAcima != "(":
                operadores.append(tokenAcima)
                tokenAcima = operador.pop()
        else:
            while (not operador.isEmpty()) and (precedencia(operador.peek()) >= precedencia(token)):
                saida.append(operador.pop())
            operador.push(token)
        
    while not operador.isEmpty():
        saida.append(operador.pop())
    return " ". join(saida)

def main():
    

if __name__ == "__main__":
    main()



