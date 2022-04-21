numero = 3
print(numero)
final = 4
contador = 1

while (contador <= 14):
    contador += 1
    teste =  final // 2
    if (teste % 2 == 0):
        numero = numero + (4/((final - 2) * (final - 1) * (final)))
    else:
        numero = numero - (4/((final - 2) * (final - 1) * (final)))
    
    final = final + 2
    print(round(numero, contador))