import random
print('Bem Vindo se você acertar o número aletario você vence !')

num = random.randint(0, 5)
print(num)

num2 = (int(input('Qual o número ?: ')))
print('Você venceu, o numero era: {}'.format(num)
      if num == num2 else 'Você perdeu o número era:{}'.format(num))
