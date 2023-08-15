from time import sleep


def contador(a, b, c):
    for i in range(a, b, c):
        print(f'{i} ', end='')
        sleep(1)


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
print()
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)

print('Agora sua vez de realizar a contagem')
ini = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(ini, f, p)
