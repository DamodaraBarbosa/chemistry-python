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
    print('2. Quantos átomos há para cada elemento.')
    print('3. Massa da espécie química.')
    print('4. Natureza elétrica da espécie química.')
    print('5. Substância orgânica ou inorgânica e seus grupamentos.')
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

def grupamentofuncional(grupamento):
    for i, l in enumerate(grupamento):
        try:
            if grupamento[i] == 'O' and grupamento[i+1] == 'H' and grupamento[i-1] != 'O' or grupamento[i] == 'H' and grupamento[i+1] == 'O' and grupamento[i+2] != 'O':
                print('Álcool')
            if grupamento[i] == 'C' and grupamento[i+1] == 'O' and grupamento[i+2] == 'O' and grupamento[i+3] == 'H' or grupamento[i] == 'H' and grupamento[i+1] == 'O' and grupamento[i+2] == 'O' and grupamento[i+3] == 'C':
                print('Ácido carboxílico')
            if grupamento[i] == 'C' and grupamento[i+1] == 'O' and grupamento[i+2] == 'O' and grupamento[i+3] == 'C' or grupamento[i] == 'C' and grupamento[i-1] == 'O' and grupamento[i-2] == 'O' and grupamento[i-3] != 'H':
                print('Éster')                                                                        
            if grupamento[i] == 'O' and grupamento[i+1] == 'C' and grupamento[i-2] == 'H' and grupamento[i-3] == 'C':
                print('Éter')
            if grupamento[i] == 'C' and grupamento[i+1]  == 'H' and grupamento[i+2] == 'O' or grupamento[i] == '0' and grupamento[i+1]  == 'H' and grupamento[i+2] == 'C':
                print('Aldeído')
            if grupamento[i] == 'O' and grupamento[i-1] == 'C':
                print('Cetona') 
            if grupamento[i] == 'N' and grupamento[i-1] == 'H' and grupamento[-2] == 'C' or grupamento[i] == 'N' and grupamento[i-1] == 'C':
                print('Amina')
        except IndexError:
            pass
