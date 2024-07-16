''' A confederação nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim         - até 19 anos: junior
- até 14 anos: infantil     - até 25 anos: senior
- acima de: master
'''
from datetime import date

ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print("mirim")
elif idade > 9 and idade <= 14:
    print("infantil")
elif idade > 14 and idade <= 19:
    print("junior")
elif idade > 19 and idade <= 25:
    print("senior")
elif idade > 25:
    print("master")
else:
    print("bad request")