from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores:', end='')
    for i in range(0, 5):
        sleep(0.3)
        n = randint(0, 12)
        lista.append(n)
        print(f' {n}', end='')
    print('\nPronto !')


numeros = list()
sorteia(numeros)


def somandopar(lista):
    soma = 0
    for valor in lista:
        sleep(0.4)
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}: a soma é {soma}')


somandopar(numeros)
