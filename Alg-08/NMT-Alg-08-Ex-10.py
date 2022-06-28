from quopri import decodestring


def decodificar(lista):
    if (len(lista) == 0):
        return []
    lista[1] -= 1
    if (lista[1] != 0):
        return list(lista[0]) + decodificar(lista)
    else:
        return list(lista[0]) + decodificar(lista[2:])

def main():
    lista = ['A', 10, 'B', 25]
    saida = decodificar(lista)
    print(saida)

if __name__=='__main__':
    main()