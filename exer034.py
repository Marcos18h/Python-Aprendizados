print('Digite seu salário e diremos seu aumento!\n Para valores acima de R$1.200 o aumento é de 10%\n Inferiores é de 15%')

salario = float(input('Digite: '))

if salario < 1200:
    aumento = (salario*15)/100
    salario1 = aumento+salario
    print('Seu aumento será de {:.2f} e o valor atualizado do seu salario é: {:.2f}'.format(
        aumento, salario1))
else:
    aumento = (salario*10)/100
    salario1 = aumento+salario
    print('Seu aumento será de {:.2f} e o valor atualizado do seu salario é: {:.2f}'.format(
        aumento, salario1))
