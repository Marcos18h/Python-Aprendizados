print('Olá meu querido digite a temperatura em grau Celsius que irei converter para Fahrenheit !')

celsius = float(input('Digite o valor em Celsius: '))

fahrenheit = ((9*celsius)/5) + 32


print('A temperatura que você digitou em graus Celsius de {:.2f} graus, equivale há {:.2f} graus Fahrenheit !'.format(
    celsius, fahrenheit))
