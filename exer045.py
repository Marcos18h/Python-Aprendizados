from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
escolha = int(input('Escolha uma opção:\n'
                    '0-Pedra\n'
                    '1-Papel\n'
                    '2-Tessoura\n'
                    'Digite: '))
if escolha > 2:
    print('Jogada Invalida !')
else:
    computador = randint(0, 2)
    print('O computador escolheu: {}'.format(itens[computador]))
    print('O jogador escolheu: {}'.format(itens[escolha]))

    if computador == 0:
        if escolha == 0:
            print('Ouve empate !')
        elif escolha == 1:
            print('Você ganhou !')
        elif escolha == 2:
            print('Você perdeu !')
    elif computador == 1:
        if escolha == 0:
            print('Você perdeu !')
        elif escolha == 1:
            print('Ouve empate !')
        elif escolha == 2:
            print('Você ganhou !')
    elif computador == 2:
        if escolha == 0:
            print('Você ganhou !')
        elif escolha == 1:
            print('Você perdeu !')
        elif escolha == 2:
            print('Ouve empate !')
