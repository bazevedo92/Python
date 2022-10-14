#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f"\033[31mErro:Por favor, digite um numero inteiro válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f"\033[31mErro:Por favor, digite um numero inteiro válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


num1 = leiaint("Digite um Inteiro: ")
num2 = leiafloat("Digite um Real: ")
print(f"O valor digitiado inteiro foi {num1} e o numero real foi {num2}")

