#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint #gerar numeros aleatorios
from operator import itemgetter

jogo = {"jogador1": randint(1, 6), #1 a 6 pq é 1 dado com 6 lados, total de 4 dados
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}
ranking = list()

print(f"Valores Sorteados: ")
for k, v in jogo.items():
        print(f"{k} tirou o valor {v} no dado")
        sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print("=== RANKING DOS JOGADORES ===")
for i, v in enumerate(ranking):
        print(f'{i+1} lugar: {v[0]} com {v[1]} pontos no dado')
        sleep(1)
