matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
nPar = somaCol3 = maiorlin2 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]: '))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            nPar += matriz[l][c]
    print()
print('-='*20)
print(f'{nPar}')
print('-='*20)
for l in range(3):
    somaCol3 += matriz[l][2]
print(f'{somaCol3}')
print('-='*20)
for c in range(3):
    if matriz[1][c] == 0:
        maiorlin2 = matriz[1][c]
    elif matriz[1][c] > maiorlin2:
        maiorlin2 = matriz[1][c]
print(f'{maiorlin2}')
