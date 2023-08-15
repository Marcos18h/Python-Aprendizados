from time import sleep
soma = 0
cont = 0
for c in range(1, 7):
    sleep(1)
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
sleep(0.5)
print('Você informou {} números pares e a soma é {}'.format(cont, soma))