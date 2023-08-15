import time

print('Bem Vindo(a) ao Programa da Tabuada!')
print('^' * 30)
while True:
    print('Caso deseje encerrar o programa digite um número < 0.')
    time.sleep(1)
    numero = int(input('Digite um número e veja sua tabuada: '))
    if numero < 0:
        break
    for n in range(0, 11):
        total = numero * n
        print(f' {numero}X{n} = {total}')
print('_' * 30)
print('FIM')
