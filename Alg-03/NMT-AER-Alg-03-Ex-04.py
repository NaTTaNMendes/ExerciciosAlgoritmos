lados = int(input("Informe a quantidade de lados: "))

if (lados < 3 or lados > 10):
    print("Valor inválido")
else:
    if(lados == 3):
        nome = "Triângulo"
    elif(lados == 4):
        nome = "Quadrilátero"
    elif(lados == 5):
        nome = "Pentágono"
    elif(lados == 6):
        nome = "Hexágono"
    elif(lados == 7):
        nome = "Heptágono"
    elif(lados == 8):
        nome = "Octágono"
    elif(lados == 9):
        nome = "Eneágono"
    elif(lados == 10):
        nome = "Decágono"
    print("Nome: ",nome)
