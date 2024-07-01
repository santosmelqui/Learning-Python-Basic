'''Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento'''

salario = float(input("Digite o salário: "))
aumento = salario * 1.15
print(f"O salário R${salario:.2f} teve um aumento de 15% e agora passou a ser R${aumento:.2f}")