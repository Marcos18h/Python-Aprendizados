def notas(*num, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param num: Uma ou maus notas dos alunos (aceita várias)
    :param sit: Analiza qual a situação do aluno (Boa, Razoável ou Ruim)
    :return: Retorna um dicionário com a situação do aluno.
    """
    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num) / len(num)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(3.4, 2.6, 4, 5, sit=True)
print(resp)

help(notas)
