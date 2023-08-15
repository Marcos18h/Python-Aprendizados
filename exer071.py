print('=' * 30)
print('Bem vindo(a), Banco MH')
print('=' * 30)
valor = int(input('Qual valor você quer sacar ? R$'))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(F'O toal de cédulas de R${cedula} foi de : {totalCedula}')
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if cedula == 0:
            break
