numero = int(input("Informe um inteiro com 3 algarismos: "))

centena = numero // 100
numero = numero - (centena * 100)

dezena = numero // 10
numero = numero - (dezena * 10)

saida = (numero * 100) + (dezena * 10) + centena

print("Valor com centenas e unidades invertidas: ", saida)

