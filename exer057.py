sexo = str(input('Digite seu sexo [M/f]')).strip().upper()[0]
cont = 0
while sexo not in 'MF':
    sexo = str(input('Dado inválido, digite novamente!: ')).strip().upper()[0]
    cont += 1
print('Sexo {} registrado com sucesso'.format(sexo))
print('Foram {} tentativas inálidas.'.format(cont))
