''' Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print(f" Sua velocidade foi de {velocidade} e você pagará R${multa} de multa")
else:
    print("Tenha um bom dia! Dirija com segurança!")