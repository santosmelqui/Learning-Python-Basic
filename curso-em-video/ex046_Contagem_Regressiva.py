'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artíficio, indo de 10 até 0, com uma pausa de 1 segungo entre
eles.
'''

from time import sleep

print("Aperte enter para contar\n\n")
input()
for c in range(10, -1, -1):
    print(c)
    sleep(1)
sleep(0.5)
print("EEEEEEE!")

