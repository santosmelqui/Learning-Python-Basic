'''
Refaça o deasfio 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''

n1 = float(input("Digite o tamanho da primeira reta: "))
n2 = float(input("Digite o tamanho da segunda reta: "))
n3 = float(input("Digite o tamanho da terceira reta: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 and n3 != n1:
        print("é um triângulo isósceles")
    elif n2 == n3 and n1 != n3:
        print("é um triângulo isósceles")
    elif n3 == n1 and n2 != n3:
        print("é um triângulo isósceles")
    elif n1 == n2 and n2 == n3 and n3 == n1:
        print("é um triângulo equilatero")
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print("é um triângulo escaleno")
    else:
        print("bad request")
else:
    print("não forma um triângulo")
