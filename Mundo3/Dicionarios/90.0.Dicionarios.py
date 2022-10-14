#pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
#pessoas['nome'] = 'Leandro' #nao precisa do append para fazer a troca
#pessoas['peso'] = 98.5
#print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas.keys():
#    print(k)

#for k, v in pessoas.items(): #parecido com o enumerate
#    print(f'{k} = {v}')



# ******* CRIANDO UM NEGOCIO DENTRO DE UMA LISTA ********

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(estado1)
#print(estado2)
#print(brasil)
#print(brasil[0])
#print(brasil[1])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade federativa: "))
    estado['sigla'] = str(input("Sigla Estado: "))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')

#    for v in e.values():
#        print(v, end='')
#    print()

