from time import sleep


def maior(* num):
    cont = mai = 0
    print('\nANALISANDO VALORES .....')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {mai}.')


maior(600, 67, 56, 33, 2, 1, 0)
maior(67, 56, 33, 2, 1, 0)
maior(56, 33, 2, 1, 0)
maior(33, 2, 1, 0)
