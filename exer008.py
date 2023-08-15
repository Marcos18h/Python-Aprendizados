metro = float(input(
    'Diga-me um valor e irei mostralo em metros, centímetros e milímetros!: '))
centimetros = metro*100
milimetros = metro*1000

print('{} metros tem {} centímetros, {:.0f} milímetros :D'.format(
    metro, centimetros, milimetros))
