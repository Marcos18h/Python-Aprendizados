from num2words import num2words

resposta = int(input('Digite um número entre 0 e 20: '))
while True:
    if resposta < 0 or resposta > 20:
        resposta = int(input('Tente novamente> Digite um número de 0 a 20: '))
    else:
        if resposta >= 0 or resposta <= 20:
            print(f'O número {resposta} por extenso é: {num2words(resposta, lang="pt-BR")}')
        para = int(input('Deseja continuar? 1:[sim], 2:[não]: '))
        if para == 1:
            resposta = int(input('Digite um número entre 0 e 20: '))
        else:
            break
