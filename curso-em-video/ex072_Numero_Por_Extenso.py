'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
'''

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
           "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
           "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    digite = int(input("Digite um número de zero a 20\n"))
    if 0 <= digite <= 20:
        print(f"Você escolheu {numeros[digite]}")
        break
    else:
        print("Bad request. Try Again")