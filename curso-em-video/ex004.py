'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele'''

a = input('Digite algo: ')

print('o tipo primitivo desse valor é: ', type(a))
print('É somente espaços: ', a.isspace())
print('É um numero: ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('É alfanumérico: ', a.isalnum())
print('Esta em maiuscula: ', a.isupper())
print('Está em minusculas: ', a.islower())
print('Esta Capitalizada: ', a.istitle())