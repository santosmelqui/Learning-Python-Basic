'''Escreva um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador. O programa deverá escrever
 na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep

pc = randint(0,5)
print("Vou pensar em um número entre 0 e 5, Eai, qual você acha que foi?\n")

num = int(input())

print("PROCESSANDO")
sleep(2)

if num == pc:
    print(f"Você acertou, pensei em {pc}")
else:
    print(f"Você errou, pensei em {pc}")