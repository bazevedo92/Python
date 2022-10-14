#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros: #se o numero digitado nao esta na lista numeros append
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]")) #resposta
    if r in "Nn": #Se a resposta for N ou n
        break
print("-=" * 30)
numeros.sort()
print(f"Você digitou os valores {numeros}")
