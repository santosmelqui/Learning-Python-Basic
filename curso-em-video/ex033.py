'''Faça um programa que leia três números e mostre qual é o maior'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f" o {n1} é maior que {n2} e que {n3}")
elif n2 > n1 and n2 > n3:
    print(f" o {n2} é maior que {n1} e que {n3}")
elif n3 > n1 and n3> n2:
    print(f" o {n3} é maior que {n1} e que {n2}")
