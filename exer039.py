from datetime import date

ano = int(input('Qual o ano de seu nascimento ?: '))

tempo = date.today().year - ano
if tempo < 18:
    print('Ainda não está na hora de se alistar!')

elif 18 == tempo:
    print('Está na hora de se alistar !')
else:
    print('Você passou da idade de se alsitar\n'
          'Procure a junta militar !')
