'''Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

num = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão\n [1] Binário\n [2] Octal\n [3] Hexadecimal\n")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é {hex(num)[:2]}")
else:
    print(f"Bad request")
