def isOrdernada(lista):
    """
    Informa se a lista está ordenada. Se ela tiver um item ou nenhum será retornado True.


    lista = list
    """
    temp = sorted(lista)

    for posicao in range(0, len(lista)):
        if (temp[posicao] != lista[posicao]):
            return False
    
    return True

def main():
    lista = []
    while True:
        item = input("Informe um item (vazio para sair): ")
        if (item == ""):
            break
        lista.append(item)
    
    if (isOrdernada(lista)):
        print("A lista está ordenada")
    else:
        print("A lista não está ordenada")

if __name__=="__main__":
    main()