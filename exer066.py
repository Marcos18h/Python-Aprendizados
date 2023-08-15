cont = numero = total = 0
while True:
    numero = int(input(f'Digit um número(999 para parar) : '))
    if numero == 999:
        break
    total += numero
    cont += 1
print(f'Foram digitados ao total {cont} números e a soma deles foi {total}')
