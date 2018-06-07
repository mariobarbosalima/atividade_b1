num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numeto: "))
num3 = int(input("Digite mais um numero: "))

if num1 > num2 > num3:
    print("Ordem crescente:" ,num3, num2, num1)
    print("Ordem decrescente:" ,num1 , num2 ,num3)
if num1 < num2 < num3:
    print("Ordem crescente:", num1, num2, num3)
    print("Ordem decrescente:", num3, num2, num1)
if num1 > num2 < num3:
    print("Ordem crescente:", num2, num1, num3)
    print("Ordem decrescente:", num3, num1, num2)
