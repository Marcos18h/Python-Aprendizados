n = []
p = []
i = []
while True:
    v = int(input('Digite um valor para ser adicionado: '))
    n.append(v)
    if v % 2 == 0:
        p.append(v)
    elif v % 2 == 1:
        i.append(v)
    r = str(input('De continuar [S/N]: ')).upper().split()
    if 'N' in r:
        break
print(f'Os números digitados foram: {n}')
print(f'Os pares foram: {p}')
print(f'Os ímpares foram: {i}')
