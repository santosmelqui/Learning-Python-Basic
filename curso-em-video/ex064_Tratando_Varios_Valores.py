'''Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

parada = 1
soma = 0
cont = 0
while parada != 999:
    n = int(input("Digite um número [999 para o programa!]: "))
    if n == 999:
        parada = n
    else:
        soma += n
        cont += 1
print(f"Você digitou {cont} números e a soma deles é {soma}")

