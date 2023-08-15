print('Olá nós somos uma empresa de aluguel de carros seja bem vindo(a) \n Os valores do aluguel são os seguintes: \n R$ 60,00 o dia \n R$ 0,15 o km rodado !')

dia = int(input('Quantos dias você rodou ?'))
km = float(input('Quantos km ?'))

diaTotal = dia*60
kmTotal = km * 0.15

total = diaTotal + kmTotal

print('Você rodou {} dias que ficou no valor de R${:.2f}, e {} km que ficou no valor de R${:.2f}, o total foi de R${:.2f} reais !'.format(
    dia, diaTotal, km, kmTotal, total))
