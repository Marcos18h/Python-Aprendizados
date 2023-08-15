alimentos = ('Bolacha Água e Sal', 3.45,
             'Água com gás', 2.50,
             'Linguiça Toscana', 17.50,
             'Arroz 7R', 22.90,
             'Feijão Preto', 5.89,
             'Pão de forma', 7.45,
             'Maça', 4.99,
             'Queijo', 15.67)
print('-=-' * 15)
print('LISTAGEM PREÇO')
print('-=-' * 15)
for posicao in range(0, len(alimentos)):
    if posicao % 2 == 0:
        print(f'{alimentos[posicao]:.<25}', end='')
    else:
        print(f'R${alimentos[posicao]:>5.2f}')
