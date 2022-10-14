#Ler 2 números, multiplica-los e apresentar o resultado caso seja o maior que 15.

print("=" * 30)
print("Vamos brincar de multiplicação")
print("=" * 30)
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 * num2

if soma > 15:
    print("O resultado da sua multiplicação foi {} ou seja foi maior que 15.".format(soma))
else:
    print("O valor da multiplicação dos seus números foi {}, ou seja menor que 15.". format(soma))