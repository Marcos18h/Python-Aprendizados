valorCasa = float(input('Boa Tarde qual o valor da casa?: '))
valorSalario = float(input('Qual o seu sálario?: '))
anos = int(input('Em quantos anos quer pagar?: '))
anosParcelas = anos * 12

valorSalario1 = valorSalario * 30 / 100
valorParcelas = valorCasa / anosParcelas

if valorParcelas > valorSalario1:
    print('Não é possivel fazer o emprestimo\n'
          'Pois a parcela de {:.2f} excedeu 30% do seu salario que é {:.2f} '.format(valorParcelas, valorSalario1))

else:
    print('Seu crédito foi aprovado!\n'
          'Suas parcelas seram de {:.2f}\n'
          'E você pagará em {} anos!'.format(valorParcelas, anos))
