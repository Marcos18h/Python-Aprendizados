termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo1 = termo
n = 1
while n <= 10:
    print('{} ->'.format(termo1), end='')
    n += 1
    termo1 += razao
