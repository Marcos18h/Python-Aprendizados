from random import shuffle

print('Olá iremos sortear a ordem de alunos para a apresentação !')
nome1 = str(input('Digite o primeiro aluno: '))
nome2 = str(input('Digite o segundo segundo: '))
nome3 = str(input('Digite o terceiro terceiro: '))
nome4 = str(input('Digite o quarto quarto: '))

nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print('O nome sorteado foi :')
print(nomes)
