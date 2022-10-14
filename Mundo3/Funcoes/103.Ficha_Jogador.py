#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f" O jogador {jog} fez {gol} gol(s) no campeonato.")

    #Programa Principal
nome = str(input("Nome do jogador: "))
num_gols = str(input("Número de Gols: "))
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0
if nome.strip() == " ":
    ficha(gol=num_gols)
else:
    ficha(nome, num_gols)
