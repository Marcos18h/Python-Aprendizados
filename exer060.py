print('Digite um número e descubra o valor do seu fatorial !')
n = int(input('Digite um número: '))
n1 = n
f = 1
while n > 0:
    print('{}'.format(n), end=' ')
    print('X' if n > 1 else '=', end=' ')
    f *= n1
    n -= 1
print('{}'.format(f))
