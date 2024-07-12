'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada'''

import random

s1 = str(input("aluno 1: "))
s2 = str(input("aluno 2: "))
s3 = str(input("aluno 3: "))
s4 = str(input("aluno 4: "))

lista = [s1,s2,s3,s4]

ordem = random.shuffle(lista)

print(lista)