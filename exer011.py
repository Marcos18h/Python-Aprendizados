print('Olá me diga quantos metros e a largura da sua parede, que irei dizer quantos litros de tinta você irá precisar para pinta-lá!')

altura = float(input('Qual a altura ?: '))
largura = float(input('Qual a largura ?: '))

metroQuadrado = largura*altura
areaPrintada = metroQuadrado/2

print('A altura de sua parede é {}, e a largura é {}, o metro quadrado total é {:.2f}, e você vai precisar de {:.0f} litros de tinta !'.format(
    altura, largura, metroQuadrado, areaPrintada))
