aluno = {'nome': str(input('Qual o nome do aluno ?: '))}
aluno['média'] = float(input(f'Qual a média do aluno {aluno["nome"]} ?: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 >= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Recuperação'

print(f'O aluno {aluno["nome"]} teve uma média de {aluno["média"]} e está {aluno["situação"]}')
