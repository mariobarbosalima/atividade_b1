x = input("digite uma operacao: ")
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))


if x == "A":
    print(num1 + num2)
if x == "S":
    print(num1 - num2)
if x == "M":
    print(num1 * num2)
if x == "D":
    if num2 != 0:
        print(num1 / num2)
    if num2 == 0:
        print("erro")
