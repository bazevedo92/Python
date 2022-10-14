#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = []
pares = []
impares = []
while True:
    num.append(int(input("Digite um numero: ")))
    resp = str(input("Quer continuar? [S / N] "))
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f"A lista completa é {num}")
print(f"Os numeros pares da lista são {pares}")
print(f"Os numeros impares da lista são {impares}")

