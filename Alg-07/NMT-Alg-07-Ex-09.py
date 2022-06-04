from random import randint

def gerarCartela():
    """
    Gera uma cartela de bingo e retorna para o usuário um dicionário com os valores gerados.
    """
    bingo = {'B': 'temp', 'I': 'temp', 'N': 'temp', 'G': 'temp', 'O': 'temp'}
    inicio = 1
    fim = 16
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

def verificarCartela(valores, bingo):
    """
    Verifica se um cartela de bingo é vencedora ou não. Retornando True caso sim.


    valores = conjunto com os números sorteados
    
    
    bingo = cartela a ser verificada 
    """
    items = set()
    valores = set(valores)
    for pos in range (0, 5):                    #Verifica todas as linhas
        for letra in bingo:
            items.add(bingo[letra][pos])
        if (items.issubset(valores)):
            return True
        items.clear()

    items.clear()
    for letra in bingo:                         #Verifica todas as colunas
        for pos in range(0, 5):
            items.add(bingo[letra][pos])
        if (items.issubset(valores)):
            return True
        items.clear()
    
    items.clear()                               #Verificam as diagonais
    inicio = -1
    for letra in bingo:
        inicio = inicio + 1
        items.add(bingo[letra][inicio])
    if (items.issubset(valores)):
        return True

    items.clear()
    inicio = -1
    for letra in "OGNIB":
        inicio = inicio + 1
        items.add(bingo[letra][inicio])
    if (items.issubset(valores)):
        return True
    
    return False

def main():
    minimo = 9999999
    maximo = 0
    qtdJogos = 1000
    totalChamadas = 0

    for rodadas in range(1, 1001):
        numerosDisponiveis = []
        for i in range(1,76):
            numerosDisponiveis.append(i)
        cartela = gerarCartela()
        NumerosSorteados = set()
        chamadas = 1
        while True:
            IndexSorteado = randint(0, len(numerosDisponiveis))
            if (IndexSorteado == len(numerosDisponiveis)):
                try:    
                    NumerosSorteados.add(numerosDisponiveis.pop())
                except:
                    break
            else:
                NumerosSorteados.add(numerosDisponiveis[IndexSorteado]) 
                del numerosDisponiveis[IndexSorteado]  

            if (chamadas >= 5) and (verificarCartela(NumerosSorteados, cartela)):
                print("Cartela vencedora: ")
                print(desenharCartela(cartela))
                print("Quantidade de números sorteados:", len(NumerosSorteados))
                print("Números sorteados:", NumerosSorteados)
                if (chamadas < minimo):
                    minimo = chamadas
                if (chamadas > maximo):
                    maximo = chamadas
                totalChamadas = totalChamadas + chamadas   
                break
            chamadas = chamadas + 1
    
    media = totalChamadas / qtdJogos
    print("Média: %.1f" % (media))
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
  
if __name__=="__main__":
    main()