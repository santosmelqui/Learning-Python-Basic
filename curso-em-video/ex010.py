'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.'''

real = float(input("Quanto você tem na carteira? "))
dolares = real / 3.27
print(f"Com R${real:.2f} você pode comprar {dolares:.2f}US$")