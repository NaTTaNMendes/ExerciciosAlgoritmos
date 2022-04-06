idade = int(input("Informe a idade do cachorro: "))

if (idade > 2):
    humana = (idade - 2) * 4 + 2 * 10.5
    print("Idade convertida: ",humana)
elif(idade < 0):
    print("Valor inválido")
else:
    humana = idade * 10.5
    print("Idade convertida: ",humana)