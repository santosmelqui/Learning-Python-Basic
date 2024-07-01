'''Faça um algoritmo que leia o preço de um produto e mostre o seu
novo preço, com 5% de desconto.'''

produto1 = float(input("Informe o preço: "))
novovalor = produto1 * 0.95
desconto = produto1 - novovalor

print(f"O valor de {produto1:.2} terá um desconto de R${desconto:.2f} e sairá por R${novovalor:.2f}")