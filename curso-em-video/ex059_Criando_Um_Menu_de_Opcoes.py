'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar             [ 2 ] multiplicar
[ 3 ] maior             [ 4 ] novos números
[ 5 ] sair do programa
'''



ciclo = 0
while ciclo != 4 and ciclo != 5:
    while ciclo != 5:
        print('''[ 1 ] somar    [ 2 ] multiplicar
[ 3 ] maior    [ 4 ] novos números
[ 5 ] sair do programa\n''')
        n1 = int(input(f"Digite o 1º número: "))
        n2 = int(input(f"Digite o 2º número: "))
        escolha = int(input("Escolha uma opção: "))
        ciclo = escolha
        if escolha == 1:
            somar = n1 + n2
            print(somar)
        elif escolha == 2:
            multiplicar = n1 * n2
            print(multiplicar)
        elif escolha == 3:
            if n1 > n2:
                print(n1)
            else:
                print(n2)
        elif escolha == 4:
            print("novos números")
        elif escolha == 5:
            print("sair do programa")
        else:
            print("escolha uma opcao valida")
