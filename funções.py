def linha():
    print('\033[1;33m--\033[m'*30)


def linha2():
    print('\033[1;33m-=\033[m'*30)


def erro():
    print('\033[1;31mDado inválido. Digite novamente!\033[m')


def cabeçalho(form):
    linha2()
    print(f'\t OPÇÕES para substância {form}')
    linha2()
    print('1. Elementos contidos na fórmula e as suas propriedades.')
    print('2. Massa molecular da substância.')