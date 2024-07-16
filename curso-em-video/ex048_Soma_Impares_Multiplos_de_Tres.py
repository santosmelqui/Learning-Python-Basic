'''
Faça um programa que calcule a soma entre todos os numeros impares que sao
multiplos de tres e que se encontram no intervalo de 1 até 500.
'''
i = 1
cont = 0
soma = 0
for c in range(i, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f"A soma de todos os {cont} valores é {soma}")
