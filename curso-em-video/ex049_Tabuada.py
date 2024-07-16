'''
RRefaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''

n1 = int(input("Digite um numero para ver sua tabuada: "))
for c in range(0,11):
    soma = n1 * c
    print(f"{n1} x {c} = {soma}")