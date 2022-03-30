valor = float(input("Investimento inicial: R$ "))

primeiro = valor * 1.12
segundo = primeiro * 1.12
terceiro = segundo * 1.12

print("Saldo em 1 ano: R$ %.2f" % primeiro)
print("Saldo em 2 anos: R$ %.2f" % segundo)
print("Saldo em 3 anos: R$ %.2f" % terceiro)
