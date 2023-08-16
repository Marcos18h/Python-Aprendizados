def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Você possui {idade} anos')
    if idade < 16:
        print('Seu voto é negado, não possui a idade minima para votar !')
    elif 16 <= idade <= 17:
        print('Seu voto é opcinal !')
    elif idade >= 70:
        print('Seu voto é opcinal !')
    else:
        print('Seu voto é obrigatório !')


voto(2006)
