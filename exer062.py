termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo1 = termo
n = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n <= total:
        print('{} ->'.format(termo1), end='')
        n += 1
        termo1 += razao
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja ver: '))
print('Progressão finalizada com {} termos'.format(total))
