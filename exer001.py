cores = {
    'amarelo': '\033[4;35;44m',
    'fundoVermelho': ' =\033[41m'
}

msg = str('Olá Mundo !')
print('{}{}'.format(cores['amarelo'], msg))
