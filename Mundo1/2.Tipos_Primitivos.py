#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor1 = input("Digite algo: ")

print("O Tipo Primitivo desse valor é {}",type(valor1))
print("Tem espaços? ",valor1.isspace())
print("É numerico? ",valor1.isnumeric())
print("É alfabético? ",valor1.isalpha())
print("É alfanumerico? ",valor1.isalnum())
print("Está em letras Maiusculas?  ",valor1.isupper())
print("Esta em letras minusculas? ",valor1.islower())
print("Esta Capitalizada? ",valor1.istitle())
