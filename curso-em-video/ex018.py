'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seo, cosseno e tangente'''

import math

angulo = float(input("Digite o ângulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}")




