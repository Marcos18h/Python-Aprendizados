print('Bom dia digite quantos km você irá viajar e falaremos o valor !\n Até 200km/h você para R$0,50 reias\n Acima você irá pagar R$0,45 reias')

km = int(input('Digite quantos km você irá percorrer: '))
if km <= 200:
    km1 = km*0.50
    print('Você irá pagar: R${:.2f}'.format(km1))
else:
    km1 = km*0.45
    print('Você irá pagar: R${:.2f}'.format(km1))
