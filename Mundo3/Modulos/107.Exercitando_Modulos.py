#Exercício Python 107: Crie um módulo chamado moeda107.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda107
p = float(input("Digite o preço: R$ "))
print(f'A metade de R$ {p} é R$ {moeda107.metade(p)}')
print(f"O dobro de R$ {p} é R$ {moeda107.dobro(p)}")
print(f"Aumentando 10%, temos R$ {moeda107.aumentar(p, 10)}")

