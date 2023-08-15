import random
print('Bem vindo tente acertar o número')
num = random.randint(1, 8)
escolha = int(input('Digite um número de 1 a 8: '))
contador = 0
while escolha != num:
    print('Tente novamente !')
    contador += 1
    if escolha < num:
        print('Mais ....')
    else:
        print('Menos ...')
    escolha = int(input('Digite um número de 1 a 8: '))
print('Parabens! Você acertou o número era: {} e você digitou: {}\n'
      'Ao todos forma {} tentativas.'.format(num, escolha, contador))
