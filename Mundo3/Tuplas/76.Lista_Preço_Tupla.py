#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("Lapis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)

print('-'*40) #coloca 30 risquinhos
print(f'{"Listagem de Preços Escolares":^40}')
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="") #.<30 = espaco de 30 pontinhos; end = adicionar o valor do fim da linha
    else:
        print(f"R${listagem[pos]:>7.2f}")
