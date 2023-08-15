numeros = []

for n in range(0, 6):
    numeros.append(int(input('Digite um número: ')))
print(f'{numeros}')

print(f'O maior número foi {max(numeros)} no índice: {numeros.index(max(numeros))+1}')
print(f'O menor número foi {min(numeros)} no índice: {numeros.index(min(numeros))+1}')
