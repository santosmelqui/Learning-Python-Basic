'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

f = ''
m = ''
while m != 'M' and f != 'F':
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    if sexo == 'M':
        print("Registrado, fim")
        m = sexo
    elif sexo == 'F':
        print("Registrado, fim")
        f = sexo
    else:
        print("Incorreto, tente outra vez!")

