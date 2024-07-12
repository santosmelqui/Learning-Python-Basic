'''Crie um programa que leia o nome de uma pessoa e diga se ela
 tem "SILVA no nome'''

nome = str(input("Digite seu nome: ").strip().lower())

tem_sim = "silva" in nome

print(tem_sim)
