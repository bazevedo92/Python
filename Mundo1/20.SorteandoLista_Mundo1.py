#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input("Nome do Primeiro Aluno: ")
n2 = input("Nome do Segundo Aluno: ")
n3 = input("Nome do Terceiro Aluno: ")
n4 = input("Nome do Quarto Aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print("A ordem de apresentacao será: {}".format(lista))
