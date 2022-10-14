#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input("Digite um número: ")),
        int(input("Digite outro número: ")),
        int(input("Digite mais um número: ")),
        int(input("Digite um último número: ")))

print(f"Você digitou os valores de {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1} posição")
else:
    print("O valor de 3 não foi encontrado em nenhuma posição")
print("Os valores pares digitados foram ", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")