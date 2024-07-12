'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome.'''

nome = str(input("Digite seu nome: ")).strip()

print("Analisando seu nome... ")

print(f"Seu nome maiúsculo é {nome.upper()} ")
print(f"Seu nome minúsculo é {nome.lower()} ")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")}")
print(f"Seu primeiro nome tem {nome.find(" ")} ")
