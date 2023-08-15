exp = str(input('Digite uma expressão:'))
pilha = []
for sim in exp:
    if sim == '(':
        pilha.append(sim)
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida !')
else:
    print('Sua expressão é invalida !')
