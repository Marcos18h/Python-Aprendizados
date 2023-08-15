valor = float(input('Quanto deu sua compra?: '))
print('Qual a forma de pagamento:\n'
      'Digite 1 para pagamento à vista\n'
      'Dinheiro/cheque com 10% de desconto!\n'
      'Digite 2 para pagamento no cartão\n'
      'Descoto de 5%\n'
      'Digite 3 em até 2x no cartão preço normal\n'
      'Digite 4, 3x ou mais no cartão\n'
      'Juros de 20%')
pagamento = int(input('Digite: '))
if pagamento == 4:
    parcelas = int(input('Em quantas vezes deseja dividir?: '))
    pag3x = valor + ((valor*20)/100)
    valorFinal = pag3x / parcelas
    print('Você irá pagar {:.2f} dividido em {}x, e o total é {:.2f}'.format(valorFinal, parcelas, pag3x))

elif pagamento == 3:
    parcelas = int(input('Em quantas vezes deseja dividir?: '))
    valorFinal = valor / parcelas
    print('Você irá pagar {:.2f} dividido em {}x, e o total é {:.2f}'.format(valorFinal, parcelas, valor))
elif pagamento == 2:
    pagCartao = valor - ((valor*5)/100)
    print('O valor é {:.2f} você irá pagar {:.2f} com 5% de desconto!'.format(valor, pagCartao))
else:
    valorDinheiro = valor - ((valor*10)/100)
    print('O valor é {:.2f} você irá pagar {:.2f} com 10% de desconto!'.format(valor, valorDinheiro))
