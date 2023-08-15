tem = []
prin = []
mai = men = 0
while True:
    tem.append(str(input('Digite o nome da pessoa: ')))
    tem.append(float(input('Digite o peso da pessoa: ')))
    if len(prin) == 0:
        mai = men = tem[1]
    elif tem[1] > mai:
        mai = tem[1]
    elif tem[1] < men:
        men = tem[1]
    r = str(input('Quer continuar [S/N]: ')).upper().split()
    prin.append(tem[:])
    tem.clear()
    if 'N' in r:
        break

print(f'Ao todos foram cadastrados: {len(prin)}')
print(f'O peso maior foi de: {mai:.2f}kg')
print('Pessoas com maior peso foram:')
for p in prin:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O peso menor foi de: {men:.2f}kg')
print('Pessoas com menor peso foram:')
for p in prin:
    if p[1] == men:
        print(f'{p[0]}')
