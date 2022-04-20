while True:
    valor = float(input("Informe o valor (0 sai do LOOP): "))
    if (valor == 0):
        break
    desconto = float(input("Informe o desconto: "))
    final = valor * (desconto/100)

    print("Valor inicial: R$%.2f | Desconto: %.2f | Valor final: R$%.2f" % (valor, desconto, final))

    

