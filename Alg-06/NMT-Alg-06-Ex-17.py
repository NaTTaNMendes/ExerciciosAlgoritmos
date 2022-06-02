def tokenise(string):
    string = string.replace(" ", "")
    numero = ''
    token = []
    for index,char in enumerate(string):

        if char in ['/','*','^','(',')','=']:
            if numero != '':
                token.append(int(numero))
            numero = ''
            token.append(char)

        elif char in ['-','+']:
            if string[index-1] in '0987654321)' and index != 0:
                if numero != '':
                    token.append(int(numero))
                numero = ''
                token.append(char)
            else:
                numero += char

        elif char in '0987654321':
            numero += char
            if index + 1 == len(string):
                if numero != '':
                    token.append(int(numero))

    return token

def isInteger(texto):
    """
    Retorna se o conteúdo de um texto é um inteiro válido
    texto = string
    """
    texto = texto.strip()

    for i in range(0, len(texto)):
        if (i == 0) and len(texto) > 1:
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
    '''
    Esse método transforma uma lista de tokens infixa para uma nova pósfixa.


    tokens = lista de tokens da expressao
    '''
    operadores = []
    postFix = []

    for token in tokens:

        token = str(token)

        if isInteger(token):
            postFix.append(token)
        
        if token in "+-*/^":
            while (len(operadores) != 0) and (operadores[-1] != "(") and (precedencia(token) <= precedencia(operadores[-1])):
                postFix.append(operadores.pop())
            operadores.append(token)
        
        if token == "(":
            operadores.append(token)
        
        if token == ")":
            while operadores[-1] != "(":
                postFix.append(operadores.pop())
            operadores.remove("(")
    
    while len(operadores) != 0:
        postFix.append(operadores.pop())
    
    return postFix

def doOperationPostFix(tokens):
    valores = []

    for token in tokens:
        token = str(token)
        if isInteger(token):
            valores.append(int(token))
        else:
            direita = valores.pop()
            esquerda = valores.pop()
            if (token == "/"):
                valores.append(esquerda / direita)
            elif (token == "+"):
                valores.append(esquerda + direita)
            elif (token == "-"):
                valores.append(esquerda - direita)
            elif (token == "*"):
                valores.append(esquerda * direita)
            elif (token == "^"):
                valores.append(esquerda ** direita)
    
    return valores[0]

def main():
    expressao = input("Informe uma expressão matemática: ")
    posFixa = infixToPosFix(tokenise(expressao))
    resultado = doOperationPostFix(posFixa)
    print("Resultado da expressão:",  resultado)
    
if __name__=="__main__":
    main()