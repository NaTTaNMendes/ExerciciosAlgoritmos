def compactar(descompactado, compactado=[]):
    if descompactado == []:
        return compactado
    compactado.append(descompactado[0])
    valor = descompactado[0]

    repeticao = 0
    for index, cada in enumerate(descompactado):
        if cada != valor:
            repeticao = index
            break
        else:
            repeticao = len(descompactado)
    
    compactado.append(repeticao)
    return compactar(descompactado[repeticao:], compactado)

def main():
    descompactada = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A']
    print(descompactada)
    print(compactar(descompactada))

if __name__=='__main__':
    main()