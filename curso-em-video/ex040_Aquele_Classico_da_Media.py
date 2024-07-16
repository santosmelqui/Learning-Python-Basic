''' Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: Reprovado
- média entre 5.0 e 6.9: Recuperação
- média 7.0 ou superior: Aprovado'''

n1 = float(input("Digite sua primeira nota: \n"))
n2 = float(input("Digite sua segunda nota: \n"))

media = (n1 + n2) / 2

if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("RECUPERAÇÃO")
elif media >= 7.0:
    print("APROVADO")
else:
    print("Bad request")