from random import randint

def gerarCartela():
    """
    Gera uma cartela de bingo e retorna para o usuário um dicionário com os valores gerados.
    """
    bingo = {'B': 'temp', 'I': 'temp', 'N': 'temp', 'G': 'temp', 'O': 'temp'}
    inicio = 1
    fim = 15
    for letra in bingo:
        valores = []
        while len(valores) < 5:
            valores.append(randint(inicio, fim))
        bingo[letra] = valores
        valores.clear
        inicio = inicio + 15
        fim = fim + 15
    
    return bingo

def desenharCartela(dados):
    """
    Retorna uma string com a cartela desenhada
    """
    cartela =            "----------------------\n"
    cartela = cartela + ("| B | I | N | G | O  |")
    for pos in range(0, 5):
        if (dados['B'][pos] < 10):            
            cartela = cartela + (f"\n| {dados['B'][pos]} " + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
        else:             
            cartela = cartela + (f"\n| {dados['B'][pos]}" + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
    cartela = cartela + "\n----------------------"    
    return cartela

def main():
    bingo = gerarCartela()
    print(bingo)
    print(desenharCartela(bingo))

if __name__=="__main__":
    main()