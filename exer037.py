print('Olá eu sou um conversor de números!')
num = int(input('Digite um número: '))
conversor = int(input('Conversões\n'
                      '1-Binário\n'
                      '2-Octal\n'
                      '3-Hexadecimal\n'
                      'Digite a conversão de sua escolha: '))
if conversor == 1:
    print('Seu numero convertido é {}'.format(bin(num)[2:]))
elif conversor == 2:
    print('Seu numero convertido é {}'.format(oct(num)[2:]))
else:
    print('Seu numero convertido é {}'.format(hex(num)[2:]))
