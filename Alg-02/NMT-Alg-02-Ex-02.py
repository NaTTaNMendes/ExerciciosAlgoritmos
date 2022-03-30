segundos = int(input("Informe a quantidade de segundos: "))

dias = segundos // (24*60*60)
segundos = segundos - (dias * (24*60*60))

horas = segundos // (60*60)
segundos = segundos - (horas * (60*60))

minutos = segundos // 60
segundos = segundos - (minutos * 60)

print("%d:%.2d:%.2d:%.2d" % (dias, horas, minutos, segundos))
