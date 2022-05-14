def verificarDataMagica(dia, mes, ano):
    """
    Verifica se uma data é mágica. (data mágica := (dia * mes) == dois ultimos digitos do ano). Retorna true caso verdade.

    dia = int

    mes = int

    ano = int
    """
    temp = str(ano)

    if (ano >= 10):       
        temp = temp[len(temp) - 2] + temp[len(temp) - 1]    
    else:
        temp = temp[len(temp) - 1]

    ano = int(temp)
    if ((dia * mes) == ano):
        return True
    else:
        return False

def verDiasNoMes(ano, mes):
    """
    Retorna a quantidade de dias na data informada.

    ano = int

    mes = int
    """
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return 31
    else:
        if ((ano % 400 == 0 or ano % 4 == 0) and mes == 2):
            return 29
        if (mes == 2):
            return 28
        return 30

def main():
    for ano in range(1900, 2000):
        for mes in range(1, 13):
            for dia in range(1, verDiasNoMes(ano, mes) + 1):
                if (verificarDataMagica(dia, mes, ano)):
                    print("%d/%d/%d" % (dia, mes, ano))

if __name__ == "__main__":
    main()