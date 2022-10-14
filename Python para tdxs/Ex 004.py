#Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

nomes = []
for c in range(10):
    nome = input("Digite um nome: ")
    nomes.append(nome)

n = input("Digite mais um nome para consulta na lista: ")
if n in nomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")


