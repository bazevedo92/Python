#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda109
p = float(input("Digite o preço: R$ "))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f"O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, True)}")
print(f"Aumentando 10%, temos {moeda109.aumentar(p, 10, True)}")
print(f"Aumentando 13%, temos {moeda109.aumentar(p, 13, True)}")


