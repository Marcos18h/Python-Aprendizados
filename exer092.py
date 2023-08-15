from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['Contrataçao:'] = int(input('Ano de contratação: '))
    dados['Sálario'] = float(input('Sálario: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contrataça'] + 35) - datetime.now().year
print('-_' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
