palavras = ('pedra', 'papel', 'fogo', 'celular', 'laranja',
            'cola', 'janela', 'garrafa', 'dado', 'caneta')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
