'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.'''

from random import randint

pc = randint(0,5)
numero = 0
cont = 0
while numero != pc:
    numero = int(input("Adivinhe o número que eu pensei entre 0 e 5: "))
    cont += 1
    if numero == pc:
        print(f"Você acertou!!! e precisou de {cont} chances")
    elif numero != pc:
        print("Tente novamente")
    else:
        print("Bad request")