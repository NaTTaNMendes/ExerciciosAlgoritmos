# O PROGRAMA LEVA EM CONSIDERAÇÃO A REGRA DE PARIDADE PAR

while True:
    pattern = input("Informe o byte (enter para sair): ")
    if (pattern == ""):
        break
    zeros = pattern.count("0")
    uns = pattern.count("1")
    if (uns % 2 == 0):
        print("Bit de paridade: 0")
    else:
        print("Bit de paridade: 1")
