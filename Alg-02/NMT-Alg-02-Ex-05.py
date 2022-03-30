troco = int(input("Informe o valor do troco: "))

cinquenta = int(troco / 50)
troco = troco - cinquenta * 50

vinteCinco = int(troco / 25)
troco = troco - vinteCinco * 25

dez = int(troco / 10)
troco = troco - dez * 10

cinco = int(troco / 5)
troco = troco - cinco * 5

print("---MOEDAS NECESSÁRIAS---")
print("50 centavos:",cinquenta)
print("25 centavos:",vinteCinco)
print("10 centavos:",dez)
print("5 centavos:",cinco)
print("1 centavo:",troco)
