print('_' * 20)
print('Program para cadastro de valores !')
print('_' * 20)
numero = []
while True:
    valor = int(input('Digite um valor para que seja cadastrado: '))
    if valor not in numero:
        numero.append(valor)
        print('O valor foi cadastrado !')
    else:
        print('Esse valor ja foi cadastrado digite outro valor !')
        valor = int(input('Digite um valor para que seja cadastrado: '))
    r = str(input('Quer continuar ? [S/N]')).upper().strip()
    if r not in 'SN':
        print('Resposta inválida!')
    elif r == 'N':
        break
print('_' * 20)
print(f'{numero}')
