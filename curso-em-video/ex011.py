'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-lo,
sabendo que cada litro de tinta pinta uma área de 2m²'''

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"A área da parede é {area} e será necessário {tinta} litros de tinta")