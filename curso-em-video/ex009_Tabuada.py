'''Faça um programa que leia um número inteiro qualquer e mostre na tla a sua tabuada'''

n1 = int(input("Escolha um número: "))

for i in range(0, 11):
    resultado = n1 * i
    print(f"{n1} * {i} = {resultado}")