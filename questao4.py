lado1 = int(input("valor para o lado1: "))
lado2 = int(input("Valor para o lado2: "))
lado3 = int(input("Valor para o lado3: "))

if (lado1 + lado2 > lado3) and (lado3 + lado2 > lado1) and (lado1 +lado3 > lado2):
    print("É um triangulo!")

    if lado1 == lado2 == lado3:
        print("É um triangulo equilatero!")

    if lado1 == lado2 != lado3:
        print("É um triangulo isoceles!")

    if lado2 == lado3 != lado1:
        print("É um triangulo isoceles!")

    if lado3 == lado1 != lado2:
        print("É um triangulo isoceles!")

    elif lado1 != lado2 != lado3:
        print("É um triangulo escaleno!")
else:
    print("Nao é um triangulo!")


