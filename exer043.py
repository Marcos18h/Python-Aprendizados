peso = float(input('Diga-me seu peso: '))
altura = float(input('Diga-me sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC:{:.2f}, você está abaixo do peso'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC:{:.2f}, você está no peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC:{:.2f}, você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC:{:.2f}, você está com obesidade'.format(imc))
else:
    print('Seu IMC:{:.2f}, você está com obesidade mórbida procure um médico')
