volume = float(input("Informe um valor em decibéis: "))

if(volume < 40):
    print("Valor muito baixo")
elif(volume > 130):
    print("Valor muito alto")
else:
    if(volume == 130):
        print("Britadeira")
    elif(volume == 106):
        print("Cortador de grama")
    elif(volume == 70):
        print("Despertador")
    elif(volume == 40):
        print("Sala silenciosa")
    elif(volume < 130 and volume > 106):
        print("Entre Britadeira e Cortador de grama")
    elif(volume < 106 and volume > 70):
        print("Entre Cortador de grama e Despertador")
    elif(volume < 70 and volume > 40):
        print("Entre Despertador e Sala silenciosa")