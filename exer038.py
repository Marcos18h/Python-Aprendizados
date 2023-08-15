num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O número {} é maior que o {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o {}'.format(num2, num1))
else:
    print('Os números {} e {} tem o mesmo valor'.format(num1, num2))
