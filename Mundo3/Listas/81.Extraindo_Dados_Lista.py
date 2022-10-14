#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resposta = str(input("Você quer continuar [S/N] "))
    if resposta in "Nn":
        break

print(f"Você digitou {len(valores)} elementos ") #len(Valores)=Contagem de quantos valores foram digitados

valores.sort(reverse=True)
print(f"A lista de valores ordenada de forma descrescente é {valores}")
if 5 in valores:
    print(f"O valor 5 faz parte da lista")
else:
    print(f"O valor 5 não foi encontrado nessa lista")