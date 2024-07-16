'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 3):
    ano_nascimento = int(input("Digite o ano de seu nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"{totmaior} são maiores e {totmenor} são menores")

