'''Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:'''

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuarr? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print("FIM DO PROGRAMA ")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato custa R${menor:.2f}")