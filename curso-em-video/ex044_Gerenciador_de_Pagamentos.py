'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e condição de pagamento:
- A vista no dinheiro: 10% de desconto,
- A vista no cartão: 5% de desconto, até 2x no cartão preço normal,
- 3x ou mais no cartão: 20% de juros'''

valor_produto = float(input('Digite o valor do produto: R$'))
print('''
Escolha uma das opções:
1 - A vista dinheiro
2 - A vista Cartão
3 - Até 2x no Cartão
4 - 3x ou mais no Cartão
''')
opcao = int(input('Opção: '))

if opcao == 1:
    valor = valor_produto * 0.9
elif opcao == 2:
    valor = valor_produto * 0.95
elif opcao == 3:
    valor = valor_produto
    parcela = valor / 2
    print(f'Sua compra será em 2x com cada parcela no valor R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    valor = valor_produto * 1.2
    numero_parcela = int(input('Digite o número de parcelas: '))
    parcela = valor / numero_parcela
    print(f'Sua compra será em {numero_parcela}x com cada parcela no valor R${parcela:.2f} COM JUROS.')
else:
    valor = 0
    print('Bad request')

print(f'Sua compra de R${valor_produto:.2f} vai custar R${valor:.2f} no final.')