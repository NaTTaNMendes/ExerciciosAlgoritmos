import random

quantidade = 0
sorteios = 0
while (quantidade < 10):     
    quantidadeCara = 0
    quantidadeCoroa = 0
    sorteioLocal = 0
    while True:
        lado = random.randint(1, 2)    
        if (lado == 1):
            print("A", end=" ")
            quantidadeCara += 1
            quantidadeCoroa = 0
        else:
            print("O", end=" ")           
            quantidadeCoroa += 1
            quantidadeCara = 0
        sorteioLocal += 1
        if (quantidadeCara == 3 or quantidadeCoroa == 3):
            print("(%.1d sorteios)" % (sorteioLocal))
            sorteios += sorteioLocal
            break
    quantidade += 1

total = sorteios / 10

print("Na média, foram necessários %.1f sorteios." % (total))