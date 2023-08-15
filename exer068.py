from random import randint

print('Bem Vindo ao jogo do PAR ou IMPAR')
print('~' * 30)
pc = randint(1, 10)
total = cont = 0

while True:
    n = int(input('Digite um número: '))
    parOuImpar = str(input('Par ou Ímpae? [P/I]')).upper().strip()[0]
    total = pc + n
    p = total % 2
    if p == 0 and parOuImpar == 'P':
        print(f'Você jogou {n} e o PC {pc} deu PAR')
        print('VOCÊ VENCEU!')
        cont += 1
    elif p == 1 and parOuImpar == 'I':
        print(f'Você jogou {n} e o PC {pc} deu PAR')
        print('VOCÊ VENCEU!')
        cont += 1
    elif p == 0 and parOuImpar == 'I':
        print(f'Você jogou {n} e o PC {pc} deu ÍMPAR')
        print('VOCÊ PERDEU!')
        print('Você escolheu Ímpar')
        break
    elif p == 1 and parOuImpar == 'P':
        print(f'Você jogou {n} e o PC {pc} deu ÍMPAR')
        print('VOCÊ PERDEU!')
        print('Você escolheu Ímpar')
        break
print(f'Você jogou {n} e o PC {pc} deu ÍMPAR')
print('VOCÊ PERDEU!')
print(f'GAME OVER ! Você venceu {cont} vezes! ')
