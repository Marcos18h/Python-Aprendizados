def ficha(jog='DESCONHECIDO', gol=0):
    print(f'O jogador {jog} fez {gol} gols.')


n = str(input('Nome do jogar: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
