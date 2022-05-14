def verificarSenha(senha):
    """
    Verifica se uma senha é válida pelos seguintes aspectos: 8 caracteres, uma maiúscula, uma minúscula e pelo menos um número. Retorna true para válida
    
    senha = string
    """
    maiuscula = 0
    minuscula = 0
    numero = 0
    for i in senha:
        if (i.isupper()):
            maiuscula += 1
        if (i.islower()):
            minuscula += 1
        if (str.isnumeric(i)):
            numero += 1

    if (minuscula < 1 or maiuscula < 1 or numero < 1 or len(senha) < 8):
        return False

    return True

def main():
    senha = input("Informe a sua senha: ")
    if (verificarSenha(senha)):
        print("Senha válida")
    else:
        print("Senha inválida")
        
if __name__ == "__main__":
    main()