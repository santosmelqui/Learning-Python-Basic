''' Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não como nome "SANTO"'''

cidade = str(input("Digite o nome de uma cidade: ")).strip().lower()

print(cidade[:5] == "santo")