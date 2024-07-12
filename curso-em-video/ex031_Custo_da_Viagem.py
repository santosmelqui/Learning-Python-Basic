'''Desenvolva um programa que pergunte a distância de uma viagem em
Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
e R$0,45 para viagens mais longas.'''

distancia = int(input("Qual a distância da viagem em Km?\n"))

if distancia <= 200:
    viagem_curta = 0.5 * distancia
    print(f"O valor é R${viagem_curta:.2f}")
elif distancia > 200:
    viagem_longa = 0.45 * distancia
    print(f"O valor é R${viagem_longa:.2f}")
else:
    print("Digite um valor válido")