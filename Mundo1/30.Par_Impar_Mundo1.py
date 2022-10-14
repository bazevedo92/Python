#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um numero: "))
resultado = num % 2 # o resto da divisao de qlqer numero par por 2 é 0 e qualquer numero impar é 2
if resultado == 0:
    print("O numero digitado é PAR")
else:
    print("O numero digitado é IMPAR")