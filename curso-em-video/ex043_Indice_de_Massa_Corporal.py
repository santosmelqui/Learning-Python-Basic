'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso    - 25 até 30: Sobrepeso
- Entre 18.5 e 25: Peso ideal       - 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m ex (1.81): ").replace(",","."))

imc = peso / (altura * altura)

print(f"O seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 >= imc < 25:
    print("Peso ideal")
elif 25 >= imc <= 30:
    print("Sobrepeso")
elif 30 > imc <= 40:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")
else:
    print("Bad request")
