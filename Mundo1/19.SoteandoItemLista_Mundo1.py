#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = input("Nome do Primeiro Aluno: ")
n2 = input("Nome do Segundo Aluno: ")
n3 = input("Nome do Terceiro Aluno: ")
n4 = input("Nome do Quarto Aluno: ")
lista = (n1, n2, n3, n4)
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))