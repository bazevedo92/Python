#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input("Qual a temperatura em C: "))
#Nao precisa de () na conta pq a ordem de precedencia matematica funciona normalmente.
fahrenheit = ((9 * temp) / 5) + 32
print("A temperatura de {}C corresponde a {}F".format(temp, fahrenheit))