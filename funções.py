def linha():
    print('--'*30)


def erro():
    print('\033[1;31mDado inválido. Digite novamente!\033[m')

def subscrito(num):
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    print(num.trans)






def cabeçalho():
    linha()
    print('OPÇÕES')
    linha()
    print('1. Elementos contidos na fórmula.')
    print('2. Massa molecular da substância.')