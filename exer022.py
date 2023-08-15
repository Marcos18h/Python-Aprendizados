print('Olá digite seu nome completo !')
nome = str(input('Digite eu nome:  '))
print('O nome com todas as letras maisculas: {}.'.format(nome.upper()))
print('O nome com todas as letras minusculas: {}.'.format(nome.lower()))
nomeDividido = nome.split()
nomeSemEspaco = "".join(nomeDividido)
print('Quantidade de letras do nome sem considerar os espaços: {};'.format(
    len(nomeSemEspaco)))
print('Quantidade de caracteres do primeiro nome: {}.'.format(
    len(nomeDividido[0])))
