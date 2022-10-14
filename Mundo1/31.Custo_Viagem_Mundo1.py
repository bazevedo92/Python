#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual e a distancia da sua viagem em KM? "))
print("Voce esta prestes a comecar uma viagem de {:.2f}KM".format(distancia))
if distancia <= 200:
    resultado1 = distancia * 0.50
    print("E o preco da sua passagem sera de R$ {:.2f}".format(resultado1))
else:
    resultado2 = distancia * 0.45
print("E o preco da sua passagem sera de R$ {:.2f}".format(resultado2))