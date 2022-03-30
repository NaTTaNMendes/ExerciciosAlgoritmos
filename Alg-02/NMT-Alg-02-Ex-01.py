dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

total = segundos + (minutos*60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print("Total de segundos: ", total)