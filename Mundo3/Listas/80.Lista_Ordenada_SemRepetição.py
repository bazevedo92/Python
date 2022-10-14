#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5): #c = contador
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]: #Se for o primeiro valor da lista so dar um append ou se o numero for maior que o ultimo elemento eu faço um lista append no final
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista): # Ele vai da posição 0 ate o ultimo da lista
            if n <= lista[pos]: #Verificar se o numero é menor igual ao ultimo valor da lista
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1 #Se sim ele adiciona na proxima posição
    print("-=" *30)
    print(f"Os valores digitados em ordem foram {lista}")

