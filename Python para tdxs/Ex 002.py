#Ler 4 números. Calcular as expressões: soma dos 2 últimos e multiplicação dos dois primeiros. Se a multiplicação dos 2 primeiros for impar exibir “a”. Se a soma dos dois últimos for par exibir “b”.


print("=" * 30)
print("Vamos brincar de matematica")
print("=" * 30)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
soma = num3 + num4
multiplicacao = num1 * num2
resultado_soma = (num3 + num4) % 2
resultado_multiplicacao = (num1 * num2) % 2

if resultado_soma == 0:
    print(f"O resultado da soma de {num3} + {num4} é par 'B' ")
else:
    print(f"O resultado da soma de {num3} + {num4} é impar")

if resultado_multiplicacao == 0:
    print(f"O resultado da multiplicação de {num1} * {num2} é par ")
else:
    print(f"O resultado da multiplicação de {num1} * {num2} é impar 'A'")


