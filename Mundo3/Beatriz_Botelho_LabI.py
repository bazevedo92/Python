from time import sleep

def gera_matriz():
    matriz = []
    valor = 1
    for l in range(8):
        linha = []
        for c in range(5):
            if l == 0 or c == 2:
                linha.append("x")
            else:
                linha.append(valor)
                valor += 1
        matriz.append(linha)
    return matriz


def forma_matriz(matriz):
    for l in range(8):
        for c in range(5):
            print(f"[{matriz[l][c]:^2}]", end=" ")
        print()


def procura_assento(matriz, num_usuario):
    for l in range(8):
        for c in range(5):
            if matriz[l][c] == num_usuario:
                posicao = (l, c)
    return posicao


matriz = gera_matriz()
vendidos = list()
disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

while True:
    try:
        print("======= POCCO BUS =======")
        print("1 - Reservar Assento")
        print("2 - Sair")
        opcao_menu = int(input("Opção [1 ou 2]: "))
        print("======= POCCO BUS =======")

        if opcao_menu == 1:
            forma_matriz(matriz)
            print()
            num_usuario = int(input("Qual assento você gostaria de reservar? "))
            if num_usuario < 1 or num_usuario > 28:
                print("\033[0;31mNúmero de assento incorreto, selecione assentos do 1 ao 28.\033[m")
                continue
            if num_usuario in vendidos:
                print("\033[0;31mDesculpe, esse assento já foi vendido.\033[m")
                sleep(1)
                continue
            if num_usuario in disponiveis:
                disponiveis.remove(num_usuario)
                vendidos.append(num_usuario)
            posicao = procura_assento(matriz, num_usuario)
            matriz[posicao[0]][posicao[1]] = "OK"
            print(f"O assento {num_usuario} foi reservado com sucesso!\n ")
            sleep(1.5)
            print("======= POCCO BUS =======")
            forma_matriz(matriz)

        elif opcao_menu == 2:
            print("Muito Obrigada por escolher a Pocco Bus")

            break
        elif opcao_menu not in "12":
            print()
    except:
        print("\033[0;31mOpção Invalida! Digite apenas 1 ou 2\n.\033[m")

if len(vendidos) == 1:
    vendidos.sort()
    print(f"O assento reservado nessa compra foi o {vendidos}")
elif len(vendidos) > 1:
    vendidos.sort()
    print(f"Você reservou {len(vendidos)} assentos nessa compra: {vendidos}")
else:
    print("        Volte Sempre")

with open("Vendidos_Pocco.txt", "w") as arquivo:
    for v in vendidos:
        arquivo.write("Assento vendido: " + str(v) + "\n")
    for v in disponiveis:
        arquivo.write("Assentos disponiveis: " + str(v) + "\n")