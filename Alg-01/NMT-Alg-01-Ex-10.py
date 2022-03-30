from math import log

a = int(input("Informe o valor de 'a': "))
b = int(input("Informe o valor de 'b': "))

soma = a + b
diferenca = b - a
produto = a * b
quociente = a // b
resto = a % b
log = log(a,10)
expoente = a ** b

print("Soma:",soma)
print("Diferença:",diferenca)
print("Produto:",produto)
print("Quociente:",quociente)
print("Resto:",resto)
print("Log de 'a':",log)
print("Expoente:",expoente)
