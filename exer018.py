from math import cos, sin, tan, radians

angulo = float(
    input('Digite o ângulo e iremos mostrar, o seno,cosseno e tangente: '))

print('Ângulo digitado foi {}, seu seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(
    angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
