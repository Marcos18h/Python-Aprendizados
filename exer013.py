print('Olá meu querido e fiel funcionário, digite o valor do seu sálario mensal e iremos repassar com um aumento de 15% !')

salario = float(input('Digite seu sálario: '))

aumento = 15/100*salario

valorFinal = salario + aumento

print('O seu sálario atual é R${:.2f}, o aumento que irá ganhar sobre os 15% será de R${:.2f}, e o valor final é de R${:.2f} reias !'.format(
    salario, aumento, valorFinal))
