'''
Desenvolva um programa que leia o primeiro termo e a razão de uma Progressao
aritmetica. No final, mostre os 10 primeiros termos dessa progressão.
'''

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimoT = termo + (10-1) * razao
for c in range(termo, decimoT + razao, razao):
    print(c, end = " -> ")
print("FIM")