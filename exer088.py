from random import randint

numDeJogos = int(input('Quantos jogos deseja sortear ?: '))
lista = list()
listaOficial = list()
quantidade = 1
while quantidade <= numDeJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    listaOficial.append(lista[:])
    lista.clear()
    quantidade += 1
print('-='*3, f'SORTEANDO {numDeJogos} JOGOS', '-='*3)
for i, l in enumerate(listaOficial):
    print(f'Jogo {i+1}: {l}')
