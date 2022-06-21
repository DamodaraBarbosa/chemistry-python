from mendeleev import element

def linha():
    print('\033[1;33m--\033[m'*30)


def linha2():
    print('\033[1;33m-=\033[m'*30)


def erro():
    print('\033[1;31mDado inválido. Digite novamente!\033[m')


def cabeçalho(form):
    linha2()
    print(f'\tOPÇÕES para substância {form}')
    linha2()
    print('1. Elementos contidos na fórmula e as suas propriedades.')
    print('2. Massa molecular da substância.')
    print('3. Quantos átomos há em cada elemento.')
    print('4. Possível(is) nome(s) para a fórmula escrita')
    print('9. Digitar uma nova fórmula de substância.')
    print('0. Finalizar o programa')
    linha()

def cabeçalhoop1():
    linha2()
    print(f'{"PROPRIEDADES DOS ELEMENTOS":>42}')
    linha2()
    print(f'{"NOME":<12}', end=' ')
    print(f'{"NÚMERO ATÔMICO (Z)":<32}', end=' ')
    print(f'{"MASSA ATÔMICA"}')
    linha()

def cabeçalhoop3():
    linha2()
    print(f'{"QUANTIDADE DE ÁTOMOS POR ELEMENTO":>45}')
    linha2()
    print(f'{"NOME":<20}', end='')
    print('QUANTIDADE DE ÁTOMOS')
    linha()


def cabeçalhoop2():
    linha2()
    print(f'{"MASSA MOLECULAR":>36}')
    linha2()
    print(f'{"FÓRMULA DA SUBSTÂNCIA":<45}', end='')
    print('MASSA (u)')
    linha()

    
    

