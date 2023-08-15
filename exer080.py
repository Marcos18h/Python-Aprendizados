n = []
for c in range(6):
    v = int(input('Digite um valor para ser adicionado na lista: '))
    if c == 0 or v > n[-1]:
        n.append(v)
    else:
        pos = 0
        while pos < len(n):
            if v <= n[pos]:
                n.insert(pos, v)
                break
            pos += 1
print(f'{n}')
