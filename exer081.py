n = []
v = int(input('Digite um valor para ser adicionado: '))
n.append(v)
while True:
    r = str(input('Deseja adicionar mais um valor [S/N]: ')).upper().split()
    print(f'{r}')
    if 'S' in r:
        v = int(input('Digite um valor para ser adicionado: '))
        n.append(v)
    elif 'N' in r:
        break
    else:
        print('Resposta inválida !')
print(f'Foram digitados {len(n)}')
print(f'Lista em ordem decrescente {sorted(n, reverse= True)}')
if 5 in n:
    print('O número 5 faz parte da lista !')
else:
    print('O número não 5 faz parte da lista !')
