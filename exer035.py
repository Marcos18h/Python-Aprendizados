print('Diga-me 3 valores e direi se é possivel formar um triângulo !')

v = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v < v2+v3 and v2 < v+v3 and v3 < v2+v:
    print('É ossivel formar um triângulo!')
else:
    print('Não é possivel formar um triângulo!')
