from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for n in numeros:
    print(f'{n} ', end=' ')

print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
