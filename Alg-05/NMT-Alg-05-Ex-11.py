import random

def gerarSenha():
    """
    Gera uma senha aleatória entre 7 e 10 caracteres. Retorna ela como string
    """
    tamanho = random.randrange(7, 11)
    saida = ""
    for i in range(0, tamanho):
        saida += chr(random.randrange(33, 127))
    return saida

def main():
    print("Senha gerada:", gerarSenha())

if __name__ == "__main__":
    main()