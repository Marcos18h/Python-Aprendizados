valores = [[], []]
valor = 0
for n in range(7):
    valor = (int(input('Digite um valor: ')))
    if valor % 2 == 0:
        valores[0].append(valor)
    elif valor % 2 == 1:
        valores[1].append(valor)
valores.sort()
valores[0].sort()
valores[1].sort()
print(f'Os valores são : {valores}')
print(f'Os pares são: {valores[0]}')
print(f'Os ímpares são: {valores[1]}')
