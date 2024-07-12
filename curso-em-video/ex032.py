''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto
'''

ano = int(input("Qual ano quer analisar?\n"))
if ano % 4 == 0 and ano % 100 and ano % 400:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")