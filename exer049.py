from time import sleep
n = int(input('Digite um número que vou mostrar sua tabuada\n'
              'Digite: '))

for c in range(0, 11):
    m = n * c
    sleep(1)
    print('{}x{} = {}'.format(n, c, m))
