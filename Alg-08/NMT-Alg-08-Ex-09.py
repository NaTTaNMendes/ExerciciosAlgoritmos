def raizQuadrada(n, estimativa=1):
    if (abs((estimativa**2) - n) <= (10**-12)):
        return estimativa
    return raizQuadrada(n,((estimativa + (n/estimativa))/2))

def main():
    print("Raíz de 2:", raizQuadrada(2))
    print("Raíz de 4:", raizQuadrada(4))
    print("Raíz de 9:", raizQuadrada(9))
    print("Raíz de 10:", raizQuadrada(10))
    print("Raíz de 25:", raizQuadrada(25))
    print("Raíz de 124:", raizQuadrada(124))
    print("Raíz de 1000:", raizQuadrada(1000))
    print("Raíz de 512:", raizQuadrada(512))
    print("Raíz de 6:", raizQuadrada(6))
    print("Raíz de 8:", raizQuadrada(8))
    print("Raíz de 81:", raizQuadrada(81))
    print("Raíz de 36:", raizQuadrada(36))

if __name__=="__main__":
    main()
