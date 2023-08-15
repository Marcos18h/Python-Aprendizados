num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
        if num % c == 0:
            print('\033[36m')
            cont += 1
        else:
            print('\033[31m')
        print('{}'.format(c))
print('\n\033[mO número {} foi divisivel {}'.format(num, cont))
if cont ==2:
    print('E por isso é um número PRIMO')
else:
    print('E por isso eçe NÃO É PRIMO ')
