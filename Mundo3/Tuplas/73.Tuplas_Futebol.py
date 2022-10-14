#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.


times = ("Corinthians", "Palmeiras", "Santos", "Gremio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atletico-PR", "Bahia",
         "São Paulo", "Fluminense", "Sport-Recife",
         "Vitoria", "Coritiba", "Avai", "Ponte Preta",
         "Atletico-GO")

print(f'Lista de time do Brasileirao: {times}')
print(f"Os 5 primeiros colocados são: {times[:5]}")
print(f"Os 4 últimos colocados são: {times[16:20]}")
print(f"Os times em ordem alfabetica são: {sorted(times)}")
print(f"O time da Chapecoense está na posição: {times.index('Chapecoense')+1}") #tem que adicionar o +1 pq a tupla começa do 0


