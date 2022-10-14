#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")

while True:
    num = int(input("Digite um numero de 0 a 10: "))
    if 0 <= num <= 10:
        break
    print("Tente novamente. ", end="") #end vazio significa que acabou
print(f"Você digitou o numero: {cont[num]}") #contagem dos numeros da cont 0, posicao 0, 1 posicao 1, por isso que ele imprimi o nome por extenso


