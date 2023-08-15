def frase(a):
    c = len(a)
    print('~' * c)
    print(f'{a}')
    print('~' * c)


for i in range(0, 3):
    fra = str(input('Escreva uma frase: '))
    frase(fra)
