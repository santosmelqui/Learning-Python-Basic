''' Crie um programa que leia um número inteiro e mostre na tela se ele
é par ou ímpar'''

num = int(input("Digite um número para verificar se é par ou ímpar: "))

if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")