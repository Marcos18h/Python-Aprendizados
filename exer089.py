ficha = list()
while True:
    nome = str(input('Qual o nome do aluno ? '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar [S/N]: ')).upper().strip()
    if r == 'N':
        break
print('-=' * 30)
print(f'{"ID":<4}{"NOME":<10}{"MEDIA":>6}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>5.1f}')
print('-=' * 30)
while True:
    r1 = int(input('Mostrar notas de qual aluno ?999 PARA : '))
    if r1 == 999:
        break
    elif r1 <= len(ficha) - 1:
        print(f'Notas de {ficha[r1][0]} são {ficha[r1][1]}')
