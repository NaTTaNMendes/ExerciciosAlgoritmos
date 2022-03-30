inteiro = int(input("Informe o inteiro com 4 dígitos: "))

milhar = inteiro // 1000
inteiro = inteiro - milhar * 1000

centena = inteiro // 100
inteiro = inteiro - centena * 100

dezena = inteiro // 10
inteiro = inteiro - dezena * 10

soma = milhar + centena + dezena + inteiro

print("Soma dos algarismos: ", soma)