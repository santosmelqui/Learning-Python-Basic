'''Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo. '''

lado1 = float(input("Qual a primeira reta? "))
lado2 = float(input("Qual a segunda reta? "))
lado3 = float(input("Qual a terceira reta? "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os segmentos podem formar um triângulo!")
else:
    print("Não podem formar um triângulo.")
