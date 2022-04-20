#FALTA TERMINAR

total = 0

while True:
    idade = input("Informe a idade (enter para parar): ")
    if (idade == ""):
        break
    idade = int(idade)
    if (idade <= 2):
        continue
    elif (idade >= 3 and idade <= 12):
        total += 14
    elif(idade >= 13 and idade )