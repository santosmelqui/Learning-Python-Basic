print("JO-KEN-PÔ")

play1 = input("Digite sua jogada, pedra, papel ou tesoura: ").lower()
play2 = input("Digite sua jogada, pedra, papel ou tesoura: ").lower()

if play1 == play2:
    print("Empate!")
elif play1 == "pedra":
    if play2 == "papel":
        print("Vitória do Player 2!")
    elif play2 == "tesoura":
        print("Vitória do Player 1!")
    else:
        print("Jogada inválida!")
elif play1 == "papel":
    if play2 == "pedra":   
        print("Vitória do Player 1!")
    elif play2 == "tesoura":
        print("Vitória do Player 2!")
    else:
        print("Jogada inválida!")
elif play1 == "tesoura":
    if play2 == "papel":
        print("Vitória do Player 1!")
    elif play2 == "pedra":
        print("Vitória do Player 2!")
    else:
        print("Jogada inválida!")
else:
    print("Jogada inválida!")

    '''Desenvolvi este código para exercitar o uso de sintaxe básica do Python, avaliei os questionamentos 
necessários para verificar se o aluno foi aprovado ou não e para descobrir quanto o aluno
necessita tirar para finalizar dentro da média proposta pela universidade.'''

print("\033[1;30;44mCálculo da média do Tecnólogo de ADS da UNIP\033[m")

while True: #Este loop é utilizado para repetição do programa quando chega ao fim
    while True:#Este segundo loop é utilizado caso o aluno erre a digitação das notas
        np1 = float(input("Digite sua primeira nota de prova: ").replace(',', '.'))
        np2 = float(input("Digite sua segunda nota de prova: ").replace(',', '.'))
        pim = float(input("Digite sua nota do PIM: ").replace(',', '.'))

        correto = str(input(f'Suas notas foram {np1}, {np2} e {pim}, correto? s/n ').lower()) #mostrando notas para conferência
        if correto == 's': #se digitar s, significa que está correto
            break
        else: #retorna para o início do 2º loop do programa
            print("Digite as notas novamente")

    media = np1 * 0.4 + np2 * 0.4 + pim * 0.2
    print(f"Sua média é: {media}")#a média proposta >= 7
    
    if pim == 0:
        print("\033[0;30;41mVocê reprovou por ter tirado 0 no PIM\033[m")#zerar no pim gera uma DP e o aluno só é aprovado após conclusão da mesma.
    elif media >= 6.7 and media <= 6.99: #média >= 6.7 será arredondada para 7 e o aluno será aprovado
        print("\033[0;30;40mAguarde que sua média será arredondada para 7\033[m")
    elif media < 6.7: # menor que 7 o aluno será submetido ao exame para recuperar a nota
        nec_exame = 10 - media
        print(f"\033[0;31mVocê precisará tirar {nec_exame} no exame para ser aprovado(a)\033[m")
        realizou = str(input("Verifique sua nota final. Já realizou o exame?  s/n ").lower())
        if realizou == 's': #caso digite s o programa prossegue
            exame = float(input("Quanto você tirou no exame? ").replace(',', '.'))
            mf = (exame + media) / 2
            if mf <= 4.75: 
                print("\033[0;30;31mVocê reprovou\033[m")
            elif mf >= 4.75 and mf < 5:#média maior que 4.75 é arredondada para 5
                print("Sua nota será arredondada para 5")
                print("\033[0;31;42mVocê foi aprovado(a)\033[m")
            else:
                print("\033[0;31;42mVocê foi aprovado(a)\033[m")
        else:
            print("Realize o exame e volte para verificar")
    else:
        print("\033[0;31;42mVocê passou\033[m") #condição referente ao primeiro if e seus elif's que possibilitam notas abaixo de 7, enquanto este else traz as notas >= 7
    
    repetir = str(input("Deseja voltar ao início? s/n ").lower()) # variável ref as primeiras linhas do código, para possível repetição do programa
    if repetir != 's':
        print("Fim. Bons estudos!")
        break