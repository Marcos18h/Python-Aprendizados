print('Olá a loja está com um desconto de 5% em qualquer produto !')
preco = float(input('Digite o preço do seu produto: '))

"""
valor dodesconto 
 valor do desconto = 100 x (5 / 100%)

valor do desconto = 100 x 0,05

valor do desconto = 5
"""
desconto = preco - (preco*5/100)

print('O preço do produto era R${}, com o valor com 5% de desconto sai por R${:.2f} !'.format(
    preco, desconto))
