fra = str(input('Digite uma frase: ')).upper().strip()

print('Na frase apareceram o A : {}'.format(fra.count('A')))
print('A letra A apareceu a primeira vez na posição: '.format(fra.find('A')+1))
print('A letra A apareceu a ultima vez na posição: '.format(fra.rfind('A')+1))
