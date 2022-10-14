#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

nome = []
peso = []
mai = men = 0

while True:
    nome.append(str(input("Digite um nome: ")))
    nome.append(float(input("Digite um peso: ")))
    if len(peso) == 0:
        mai = men = nome[1] #temp 2 porque a posição 2 é o peso que pede no exercicio
    else:
        if nome[1] > mai:
            mai = nome[1]
        if nome[1] < men:
            men = nome[1]
    peso.append(nome[:])
    nome.clear()
    resposta = str(input("Deseja adicionar mais uma pessoa? [S / N]"))
    if resposta in "Nn":
        break

print("-=" * 30)
print(f"Os dados foram {peso}")
print(f"Você cadastrou {len(peso)} pessoas")
print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
for p in peso:
    if p[1] == men:
        print(f"[{p[0]}", end="")
print()
