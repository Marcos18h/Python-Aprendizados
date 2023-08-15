print('Diga-me 3 valores e direi se é possivel formar um triângulo !')

v1: int = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v2 + v1:
    print('É possivel formar um triângulo!')
    if ((v1 == v2) and (v1 != v3)) or ((v1 == v3) and (v1 != v2) or ((v3 == v2) and (v1 != v3))):
        print('Esse é um triangulo Isóceles')
    elif v1 == v2 == v3:
        print('Esse é um triagulo Equilátero')
    else:
        print('Esse é um triangulo Escaleno')
else:
    print('Não é possivel formar um triângulo!')
