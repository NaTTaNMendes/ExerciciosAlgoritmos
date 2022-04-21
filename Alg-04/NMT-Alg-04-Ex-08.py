mensagem = input("Informe a mensagem: ").upper()
deslocamento = int(input("Informe o deslocamento: "))

saida = ""
tamanho = len(mensagem)
i = 0

while (i < tamanho):
    numero = ord(mensagem[i])
    total = numero + deslocamento

    if (total > ord("Z")):
        conversao = (deslocamento - (ord("Z") - numero)) + (ord("A") - 1)
    elif (total < ord("A")):
        if(total == 64):
            conversao = ord("Z")
        else:
            conversao = ord("Z") - ((ord("A") - total))
    else:
        conversao = numero + deslocamento

    saida = saida + chr(conversao)
    i += 1

print(saida)