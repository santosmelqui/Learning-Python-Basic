'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

clubes = ("botafogo", "Palmeiras", "Flamengo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Athletico-PR",
          "Bragantino", "Atlético-MG", "Vasco da Gama", "Juventude", "Interncaional", "Corinthians",
          "Criciúma", "Cuiabá", "EC Vitória", "Gremio", "Fluminense", "Atlético-GO")

print(f"Os 5 primeiros times são: {clubes[0:5]}")

print(f"Os 4 últimos colocados são: {clubes[-4:]}")

print(f"Os times em ordem alfabética: {sorted(clubes)}")

print(f"O corinthians está na {clubes.index("Corinthians")+1}ª posição")
