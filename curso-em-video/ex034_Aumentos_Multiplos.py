'''Faça um programa que pergunte o salário de um funcionário e calcule
 o valor de seu aumento. Para salários superiores a R$1250,00, calcule
 um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input("Qual o seu salário? \n"))

if salario > 1250:
    aumento10 = salario * 1.10
    print(aumento10)
elif salario <= 1250:
    aumento15 = salario * 1.15
    print(aumento15)
else:
    print("Bad request")