''' Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da csa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado'''

valor_da_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = float(input("Em quantos anos você vai pagar? "))

meses = anos * 12

prestacao = valor_da_casa / meses

porcento = salario - (salario * 0.7)

print(f"Para pagar uma casa de R${valor_da_casa:.2f} em {anos} anos\n A prestação será de R${prestacao:.2f}")

print("Analisando...")

if prestacao < porcento:
    print("Negado")
elif prestacao >= porcento:
    print("Aceito")
else:
    print("Bad request")