salario = float(input("Digite um valor: "))
valor_total = 0

if salario < 280:
    valor_total = ((salario * 0.2) + salario)
    print("O percentual de aumento foi de 20%")
if salario > 280 and salario <= 700:
    valor_total = ((salario * 0.15) + salario)
    print("O percentual de aumento foi de 15%")
if salario > 700 and salario <= 1500:
    valor_total = (( salario * 0.1) + salario)
    print("O percentual de aumento foi de 10%")
if salario > 1500 :
    valor_total = ((salario * 0.05) + salario)
    print("O percentual de aumento foi de 5%")
print("O salario apos o aumento vai ser R$" ,valor_total,)
print("O salario antes do reajuste e R$" ,salario,)
print("O valor do aumento e de R$", valor_total - salario,)
