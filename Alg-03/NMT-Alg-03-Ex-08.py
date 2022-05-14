'''O PROGRAMA ESTÁ ACEITANDO TODAS AS CASAS'''

nota = input("Informe a nota e a casa: ")
nota = nota.upper()

casa = int(nota[1])

if(nota[0] == 'A'):
    frequencia = 440 / (2 ** (4 - casa))
elif(nota[0] == 'B'):
    frequencia = 493.88 / (2 ** (4 - casa))
elif(nota[0] == 'C'):
    frequencia = 261.63 / (2 ** (4 - casa))
elif(nota[0] == 'D'):
    frequencia = 293.66 / (2 ** (4 - casa))
elif(nota[0] == 'E'):
    frequencia = 329.23 / (2 ** (4 - casa))
elif(nota[0] == 'F'):
    frequencia = 349.23 / (2 ** (4 - casa))
elif(nota[0] == 'G'):
    frequencia = 392 / (2 ** (4 - casa))

print("Frequência de %s: %.2fHz" % (nota, frequencia))