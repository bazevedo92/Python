#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei? ")) #Jogador tenta adivinha qual o  numero pensado pelo pc
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Você acertou, conseguiu me vencer! ")
else:
    print("Voce errou, tente de novo!")
