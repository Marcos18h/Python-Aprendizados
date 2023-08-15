print('Bem vido digite um número e falaremos se é par ou ímpar !')

num = int(input('Digite: '))
num1 = num % 2

print('O número {} é par'.format(num) if num1 ==
      0 else 'O número é impar'.format(num))
