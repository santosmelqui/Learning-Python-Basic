'''Faça um programa que leia o nome completo de uma pessoa, mostrando
 em seguida o primeiro e o último nome separadamente

 Ex: Ana Maria de Souza
 prmeiro = Ana
 último = Souza'''

nome = str(input("Digite seu nome: ")).strip()
separa = nome.split()

print(f"Seu primeiro nome é {separa[0]} e seu último nome é {separa[-1]}")
