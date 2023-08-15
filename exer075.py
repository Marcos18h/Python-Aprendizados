n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite mais outro valor: '))
n5 = int(input('Digite outro valor: '))
numeros = (n1, n2, n3, n4, n5)

print(f'Você digitou os números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)}')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares foram: ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
