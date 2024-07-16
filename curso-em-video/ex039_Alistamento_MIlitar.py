'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: \n"))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if ano_nascimento == 18:
    print("Você fará esse ano o alistamento militar")
elif ano_nascimento > 18:
    passou = idade - 18
    print(f"Você já passou {passou} ano(s) do prazo")
elif ano_nascimento < 18:
    ainda = idade - 18
    print(f"Ainda falta(m) {ainda} ano(s) do prazo")
else:
    print("Bad request")