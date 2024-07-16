'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o.
'''
soma = 0
for c in range(1,7):
    n1 = int(input("Digite seis números inteiros: "))
    if n1 % 2 == 0:
        soma += n1
print(soma)