#Faça um algoritmo para ler 20 números e os armazene em um vetor. Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.


list = []
for c in range(20):
    valor = input("Digite uma nota: ")
    list.append(valor)
    continue
print(f"Os números digitados foram {list}")
list.sort(reverse=True)
print(f"A ordem inversa desses números é {list}")