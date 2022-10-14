#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Largura da Parede: "))
altura = float(input("Altura da Parede: "))
area = largura * altura

print("Sua parede tem a dimensão de {} x {} e sua área é de {}m2.".format(largura, altura, area))
print("Para pintar essa parede, você precisará de {}L de tinta.".format(area / 2))
