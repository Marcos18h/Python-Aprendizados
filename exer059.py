num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    opcao = int(input('O que deseja realizar:\n'
                      '[1] somar\n'
                      '[2] multiplicar\n'
                      '[3] maior\n'
                      '[4] novos números\n'
                      '[5] sair do programa: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if opcao == 1:
        soma = num1 + num2
        print('A soma dos valores é: {}'.format(soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação dos valores é: {}'.format(multiplicacao))
    elif opcao == 3:
        if num1 < num2:
            print('O número {} é maior'.format(num2))
        else:
            print('O número {} é maior'.format(num1))
    elif opcao == 4:
        num1 = int(input('Digite o novo valor do primeiro número: '))
        num2 = int(input('Digite o novo valor do segundo número: '))
    elif opcao > 5:
        print('Opção  inválida !')
print('Obrigado por participar !')
