#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#3.17
import math
angulo = float(input("Digite o ângulo que você deseja: "))
# a medida do angulo esta em graus, é necessario converter para radiano para fazer o calculo

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo,seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo,cosseno))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(angulo,tangente))