data = int(input("Informe a data (DDMMAA): "))

dezenaDia = data // 100000
data = data - (dezenaDia * 100000)

unidadeDia = data // 10000
data = data - (unidadeDia * 10000)

dezenaMes = data // 1000
data = data - (dezenaMes * 1000)

unidadeMes = data // 100
data = data - (unidadeMes * 100)

dezenaAno = data // 10
data = data - (dezenaAno * 10)

saida = (data * 10000) + (dezenaAno * 100000) + (unidadeMes * 100) + (dezenaMes * 1000) + (unidadeDia * 1) + (dezenaDia * 10)

print("Valor invertido: ",saida)