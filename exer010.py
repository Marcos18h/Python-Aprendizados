print('Olá me diga quanto você tem em dinheiro R$, que irei converter para dólares US$ :D')
print('Preço atual do dólar: US$ 1 = R$ 5')
saldo = int(input('Quanto você possui em reias R$: '))
conversor = saldo/5

print('Você pode comprar com R${} reias, US${:.2f} dólares'.format(saldo, conversor))
