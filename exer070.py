totalGasto = menorValor = contProduto = produtosCustMil = 0
produtoBarato = ' '
while True:
    nomeProduto = str(input('Qual o nome do produto? :'))
    valorProduto = float(input('Qual valor do produto ? '))
    contProduto += 1
    totalGasto += valorProduto
    if valorProduto >= 1000:
        produtosCustMil += 1
    if contProduto == 1 or valorProduto < menorValor:
        menorValor = valorProduto
        produtoBarato = nomeProduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Tem mais algum produto [S/N] ?')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra foi R$ {totalGasto}')
print('-'*40)
print(f'O total de produtos acima de R$ 1.000 foi : {produtosCustMil}')
print('-'*40)
print(f'O produto mais barato foi : {produtoBarato}')
