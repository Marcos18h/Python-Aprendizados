print('Bom dia ! Eusou o radar caso passe a mais de 80Km/h você será multado !')

v = float(input('Há qual velocidade você passou ?'))
multa = (v-80)*7

print('Você foi mudado e pagara R$7,00 por km exedido. VALOR SERÁ DE: R${:.0f},00!'.format(multa) if v > 80 else 'Segue !')