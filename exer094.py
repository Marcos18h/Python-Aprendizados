galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] : ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('---'*12)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end=' ')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')
print()
print('Lista de pessoas que estão acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print('    ', end=' ')
        for k, v in pessoa.items():
            print(f'{k} = {v}:', end=' ')
        print()
print('ENCERRADO >> ')
