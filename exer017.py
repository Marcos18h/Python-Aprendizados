from math import hypot

print('Digite o cateto oposto e o cateto adjacente e iremos mostrar a hipoterusa!')

opos = float(input('Digite o coseno: '))
adja = float(input('Digite o seno: '))

print('A hipoterusa desse triangulo retangulo é: {:.2f}'.format(
    hypot(opos, adja)))
