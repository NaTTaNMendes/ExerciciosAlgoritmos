mes = input("Informe o mês: ")
mes = mes.upper()

if (mes == "JANEIRO"):
    dias = 31
elif(mes == "FEVEREIRO"):
    dias = "28 ou 29"
elif(mes == "MARÇO"):
    dias = 31
elif(mes == "ABRIL"):
    dias = 30
elif(mes == "MAIO"):
    dias = 31
elif(mes == "JUNHO"):
    dias = 30
elif(mes == "JULHO"):
    dias = 31
elif(mes == "AGOSTO"):
    dias = 31
elif(mes == "SETEMBRO"):
    dias = 30
elif(mes == "OUTUBRO"):
    dias = 31
elif(mes == "NOVEMBRO"):
    dias = 30
elif(mes == "DEZEMBRO"):
    dias = 31

print(mes, "possui", dias, "dias")