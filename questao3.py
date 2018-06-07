p1 = str(input("Telefonou para a vitima? "))
p2 = str(input("Esteve no local do crime? "))
p3 = str(input("Mora perto da vitima? "))
p4 = str(input("Devia para a vitima? "))
p5 = str(input("Ja trabalhou com a vitima? "))
acumulador = 0

if p1 == "S":
    acumulador = acumulador +1
if p2 == "S":
    acumulador = acumulador +1
if p3 == "S":
    acumulador = acumulador +1
if p4 == "S":
    acumulador = acumulador +1
if p5 == "S":
    acumulador = acumulador +1


if acumulador == 1:
    print("Voce é inocente!")

if acumulador == 2:
    print("Voce é um suspeito!")

if acumulador == 3 or acumulador == 4:
    print("Voce foi cumplice!")

if acumulador == 5:
    print("Voce é o assassino!")
