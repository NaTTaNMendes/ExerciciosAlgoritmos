def buscaReversa(valor, dicionario):
    """
    Retorna todas as chaves mapeadas para o valor informado.
    """
    lista = []
    for k,v in dicionario.items():
        if v == valor:
            lista.append(k)

    return lista
    
def main():
    dicionario = {'valor': 2, 'valor2': 3, 'valor3': 4, 'valor4': 2, 'valor5': 2}
    valor = 2
    lista = buscaReversa(valor, dicionario)
    if (len(lista) == 0):
        print("Nenhum valor encontrado")
    else:
        print("Valores encontrados:", lista)

if __name__=="__main__":
    main()
    