soma = cont = menor = maior = media = 0
r = 'S'
while r in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar [S]/[N] ? ')).upper()
media = soma / cont
print('Foram lidos {} e a média foi de {:.2f}'.format(cont, media))
print('_'*40)
print('O maior número foi {} e o menor {}.'.format(maior, menor))
print('Fim')

"""resp = 'S'

soma = quantide = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantide += 1

    resp = str(input('Quer continuar ? [s]/[n]')).upper().strip()[0]
media = soma / quantide
print('Você digitou {} números e a média foi {}'.format(quantide,media))"""
