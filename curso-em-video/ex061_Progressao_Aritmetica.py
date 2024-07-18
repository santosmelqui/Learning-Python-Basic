'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
'''

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo_termo = primeiro_termo + (10-1) * razao
termo = primeiro_termo
cont = 1
while cont <= 10:
   print(f"{termo} ")
   termo += razao
   cont += 1
print("FIM")
