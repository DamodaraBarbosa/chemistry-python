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

def funíon(mostrada):
    for i, v in enumerate(mostrada):
        if v == '+':
            mostrada[i] = '⁺'
        elif v == '-':
            mostrada[i] = '⁻'
        if str(v) == '₁' and mostrada[i-1] == '⁺' or str(v) == '₁' and mostrada[i-1] == '⁻':
            mostrada[i] = '¹'
        elif str(v) == '₂' and mostrada[i-1] == '⁺' or str(v) == '₂' and mostrada[i-1] == '⁻':
            mostrada[i] = '²'
        elif str(v) == '₃' and mostrada[i-1] == '⁺' or str(v) == '₃' and mostrada[i-1] == '⁻':
            mostrada[i] = '³'
        elif str(v) == '₄' and mostrada[i-1] == '⁺' or str(v) == '₄' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁴'
        elif str(v) == '₅' and mostrada[i-1] == '⁺' or str(v) == '₅' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁵'
        elif str(v) == '₆' and mostrada[i-1] == '⁺' or str(v) == '₆' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁶'
        elif str(v) == '₇' and mostrada[i-1] == '⁺' or str(v) == '₇' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁷'
        elif str(v) == '₈' and mostrada[i-1] == '⁺' or str(v) == '₈' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁸'
        elif str(v) == '₉' and mostrada[i-1] == '⁺' or str(v) == '₉' and mostrada[i-1] == '⁻':
            mostrada[i] = '⁹'

def valencia(formulaion):
    for i, v in enumerate(formulaion):
        if v == '+' or v == '-':
            carga = v
        if i == len(formulaion)-1 and v == '1':
            print(f'monovalente ({carga}1)')
        elif i == len(formulaion)-1 and v == '2':
            print(f'bivalente  ({carga}2)')
        elif i == len(formulaion)-1 and v == '3':
            print(f'trivalente ({carga}3)')
        elif i == len(formulaion)-1 and v == '4':
            print(f'tetravalente ({carga}4)')
        elif i == len(formulaion)-1 and v == '5':
            print(f'pentavalente ({carga}5)')
        elif i == len(formulaion)-1 and v == '6':
            print(f'hexavalente ({carga}6)')
        elif i == len(formulaion)-1 and v == '7':
            print(f'heptavalente ({carga}7)')
        elif i == len(formulaion)-1 and v == '8':
            print(f'octavalente ({carga}8)')
        elif i == len(formulaion)-1 and v == '9':
            print(f'nonavalente ({carga}9)')
            


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


def cabeçalhoop4(formulasobrescrita):
    linha2()
    print(f'{"NATUREZA ELÉTRICA":>36}')
    linha2()
    print(f'{"ESPÉCIE QUÍMICA":<50}', end='')
    print(formulasobrescrita)
    linha()


def grupamentofuncional(grupamento):
    for i, v in enumerate(grupamento):
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
