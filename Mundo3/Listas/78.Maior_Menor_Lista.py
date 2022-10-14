#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []
maior = 0
menor = 0
for c in range(0, 5): #c= contagem
    listanum.append(int(input(f"Digite um valor para a Posição {c}: "))) #adicionando os valores no final
    if c == 0: #Se ele for o primeiro numero digitado ele é o meior e menor tbm
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior: #Se o valor que acabei de ler é maior que o maior valor ele entra na posicao c
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print("=-" * 30)
print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior} na posição ", end=" ")
for i, v in enumerate(listanum): # i=indice , v=valor
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} na posição ", end=" ")
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}...", end=" ")