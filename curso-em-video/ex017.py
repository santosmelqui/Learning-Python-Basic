'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjascente de um triângulo retângulo, calcule e mostre o
 comprimento da hipotenusa.'''

import math

a = float(input("Diite o cateto oposto: "))
b = float(input("Digite o cateto adjascente: "))

hipotenusa = math.sqrt(pow(2,a) + pow(2,b))

print(f"A hipotenusa é igual a {hipotenusa:.2f}")