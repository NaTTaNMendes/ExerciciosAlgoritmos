pequeno = int(input("Menores que 1 litro:"))
grande = int(input("Maiores que 1 litro:"))

total = (pequeno * 0.1) + (grande * 0.25)

print("Total: R$ %.2f" % total)
