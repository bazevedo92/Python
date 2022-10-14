#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda109
p = float(input("Digite o preço: R$ "))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.moeda(moeda109.metade(p))}')
print(f"O dobro de {moeda109.moeda(p)} é {moeda109.moeda(moeda109.dobro(p))}")
print(f"Aumentando 10%, temos {moeda109.moeda(moeda109.aumentar(p, 10))}")

