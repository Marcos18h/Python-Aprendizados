print('Programa de cadastro !')
print('~' * 30)
pessoasCom18 = contadorHomens = mulherMenor20 = 0
while True:
    idade = int(input('Qual a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]: ')).upper().strip()[0]
        if idade >= 18:
            pessoasCom18 += 1
        if sexo == 'M':
            contadorHomens += 1
        if sexo == 'F' and idade < 20:
            mulherMenor20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Foram cadastrados {pessoasCom18} maiores de 18 ano!')
print('-' * 30)
print(f'Foram cadastrados {contadorHomens} homens !')
print('-' * 30)
print(f'E foram cadastradas {mulherMenor20} mulheres com menos de 20 anos !')
