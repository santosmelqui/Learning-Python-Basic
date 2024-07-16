'''
Faça um programa que leia um numero inteiro e diga se ele é ou não um
numero primo
'''
cont = 0
n1 = int(input("Digite um número inteiro: "))
for c in range(1, n1+1):
    if n1 % c == 0:
        print(f"\033[35m", end='')
        cont += 1
    else:
        print(f"\033[32m", end='')
    print(c, end='')
print(f"\n \033[mO número {n1} foi dividido {cont} vezes")
if cont == 2:
    print("Por isso ele é primo")
else:
    print("Não é primo")