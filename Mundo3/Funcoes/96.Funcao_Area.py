#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f"A area de um terreno de {largura} larg x {comprimento} comprimento é de {a}m")

def escreva(msg):
    tam = len(msg)
    print("-=" * tam)
    print(msg)
    print("-=" * tam)


escreva("Calculadora de Terrenos")
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)