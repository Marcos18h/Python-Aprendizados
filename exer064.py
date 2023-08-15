num = cont = soma = 0
print('Digitando e somando .....')
print('_'*30)
num = int(input('Digite um número: '))
print('-'*30)
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite outro numero: '))
    print('Se quiser parar digite 999 !')
    print('Você digitou {} e o valor total foi de {}'.format(cont, soma))
