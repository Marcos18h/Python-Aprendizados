nota1 = float(input('Qual sua primeira nota ?: '))
nota2 = float(input('Qual sua segunda nota ?: '))

media = float((nota1+nota2)/2)


if media < 5:
    print('Você foi reprovado estude mais!\n'
          'Sua média: {:.2f}'.format(media))
elif media >= 5 or media <= 6.9:
    print('Você está de recuperação!\n'
          'Sua média: {:.2f}'.format(media))
else:
    print('Parabéns você está aprovado!\n'
          'Sua média: {:.2f}'.format(media))
