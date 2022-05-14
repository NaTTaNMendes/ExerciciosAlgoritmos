mes = input("Informe o mês: ")
mes = mes.upper()
dia = int(input("Informe o dia: "))

if(mes == "JANEIRO"):
    if(dia == 1):
        print("Confraternização universal")
    else:
        print("Não é feriado")
elif(mes == "ABRIL"):
    if(dia == 21):
        print("Tiradentes")
    else:
        print("Não é feriado")
elif(mes == "MAIO"):
    if(dia == 1):
        print("Dia do trabalho")
    else:
        print("Não é feriado")
elif(mes == "SETEMBRO"):
    if(dia == 7):
        print("Independência do Brasil")
    else:
        print("Não é feriado")
elif(mes == "OUTUBRO"):
    if(dia == 12):
        print("Nossa Senhora Aparecida")
    else:
        print("Não é feriado")
elif(mes == "NOVEMBRO"):
    if(dia == 2):
        print("Finados")
    elif(dia == 15):
        print("Proclamação da República")
    else:
        print("Não é feriado")
elif(mes == "DEZEMBRO"):
    if(dia == 25):
        print("Natal")
    else:
        print("Não é feriado")
else:
    print("Não é feriado")