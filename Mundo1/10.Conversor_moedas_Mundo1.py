#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input("Quanto de dinheiro você tem na carteira? R$ "))
dolar = money / 3.27

print("Com o valor de R$ {:.2f} que você tem em carteira, vocë consegue comprar USD {:.2f}.".format(money, dolar))
