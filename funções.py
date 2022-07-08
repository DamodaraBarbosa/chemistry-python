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


def nomenclaturaíon(formulaion):
    nomenclatura_cátions = [{'cátion': 'Li⁺', 'nomenclatura': 'lítio'}, {'cátion': 'Na⁺', 'nomenclatura': 'sódio'}, {'cátion': 'K⁺', 'nomenclatura': 'potássio'}, {'cátion': 'Rb⁺', 'nomenclatura': 'rubídio'}, {'cátion': 'Cs⁺', 'nomenclatura': 'césio'}, {'cátion': 'Fr⁺', 'nomenclatura': 'frâncio'}, {'cátion': 'Ag⁺', 'nomenclatura': 'prata'}, {'cátion': 'Cu⁺', 'nomenclatura': 'cobre ou cuproso'}, {'cátion': 'Au⁺', 'nomenclatura': 'ouro'}, {'cátion': 'NH₄⁺', 'nomenclatura': 'amônio'}, {'cátion': 'Be⁺²', 'nomenclatura': 'berílio'}, {'cátion': 'Mg⁺²', 'nomenclatura': 'magnésio'}, {'cátion': 'Ca⁺²', 'nomenclatura': 'cálcio'}, {'cátion': 'Sr⁺²', 'nomenclatura': 'estrôncio'}, {'cátion': 'Ba⁺²', 'nomenclatura': 'bário'}, {'cátion': 'Rd⁺²', 'nomenclatura': 'rádio'}, {'cátion': 'Zn⁺²', 'nomenclatura': 'zinco'}, {'cátion': 'Cd⁺²', 'nomenclatura': 'cádmio'}, {'cátion': 'Cu⁺²', 'nomenclatura': 'cobre (II) ou cupríco'}, {'cátion': 'Hg⁺²', 'nomenclatura': 'mercúrio (II) ou mercúrico'}, {'cátion': 'Fe⁺²', 'nomenclatura': 'ferro (II) ou ferroso'}, {'cátion': 'Co⁺²', 'nomenclatura': 'cobalto'}, 
    {'cátion': 'Ni⁺²', 'nomenclatura': 'níquel (II) ou niqueloso'}, {'cátion': 'Cr⁺²', 'nomenclatura': 'cromo (II) ou cromoso'}, {'cátion': 'Mn⁺²', 'nomenclatura': 'manganês (II) ou manganoso'}, {'cátion': 'Sn⁺²', 'nomenclatura': 'estanho(II) ou estanhoso'}, {'cátion': 'Pb⁺²', 'nomenclatura': 'chumbo (II) ou plumboso'}, {'cátion': 'Ti⁺²', 'nomenclatura': 'titânio (II) ou titanoso'}, {'cátion': 'Pt⁺²', 'nomenclatura': 'platina (II) ou platinoso'}, {'cátion': 'Al⁺³', 'nomenclatura': 'alumínio'}, {'cátion': 'Bi⁺³', 'nomenclatura': 'bismuto'}, {'cátion': 'Au⁺³', 'nomenclatura': 'ouro (III) ou áurico'}, {'cátion': 'Fe⁺³', 'nomenclatura': 'ferro (III) ou férrico'}, {'cátion': 'Co⁺³', 'nomenclatura': 'cobalto (III) ou cobáltico'}, {'cátion': 'Ni⁺³', 'nomenclatura': 'níquel (III) ou niquélico'}, {'cátion': 'Cr⁺³', 'nomenclatura': 'cromo (III) ou crômico'}, {'cátion': 'Sn⁺⁴', 'nomenclatura': 'estanho (IV) ou estânico'}, {'cátion': 'Pb⁺⁴', 'nomenclatura': 'chumbo (IV) ou plúmbico'}, {'cátion': 'Ti⁺⁴', 'nomenclatura': 'titânio (IV) ou titânico'}, {'cátion': 'Pt⁺⁴', 'nomenclatura': 'platina (IV) ou platínico'}, 
    {'cátion': 'Mn⁺⁴', 'nomenclatura': 'manganês (IV) ou mangânico'}, {'cátion': 'Cr⁺⁶', 'nomenclatura':'cromo (VI)'}]
    nomenclatura_ânions = [{'ânion': 'F⁻', 'nomenclatura': 'fluoreto'}, {'ânion': 'Cl⁻', 'nomenclatura': 'cloreto'}, {'ânion': 'Br⁻', 'nomenclatura': 'brometo'}, {'ânion': 'I⁻', 'nomenclatura': 'iodeto'}, {'ânion': 'ClO⁻', 'nomenclatura': 'hipoclorito'}, {'ânion': 'ClO₂⁻', 'nomenclatura': 'clorito'}, {'ânion': 'ClO₃⁻', 'nomenclatura': 'clorato'}, {'ânion': 'ClO₄⁻', 'nomenclatura': 'perclorato'}, {'ânion': 'BrO⁻', 'nomenclatura': 'hipobromito'}, {'ânion': 'BrO₃⁻', 'nomenclatura': 'bromato'}, {'ânion': 'IO⁻', 'nomenclatura': 'hipoiodito'}, {'ânion': 'IO₃⁻', 'nomenclatura': 'iodato'}, {'ânion': 'IO₄⁻', 'nomenclatura': 'periodato'}, {'ânion': 'CN⁻', 'nomenclatura': 'cianeto'}, {'ânion': 'OCN⁻', 'nomenclatura': 'cianato'}, {'ânion': 'SCN⁻', 'nomenclatura': 'tiocianato'}, {'ânion': 'CH₃COO⁻', 'nomenclatura': 'acetato'}, {'ânion': 'C₂H₃O₂⁻', 'nomenclatura': 'acetato'}, {'ânion': 'CO₃⁻²', 'nomenclatura': 'carbonato'}, {'ânion': 'HCO⁻²', 'nomenclatura': 'formiato'},  {'ânion': 'HCO₃⁻', 'nomenclatura': 'bicarbonato'}, {'ânion': 'C₂O₄⁻²', 'nomenclatura': 'oxalato'}, {'ânion': 'C₂⁻²', 'nomenclatura': 'carbeto ou acetileto'}, 
    {'ânion': 'C⁻⁴', 'nomenclatura': 'carbeto ou metileto'}, {'ânion': 'NO₂⁻', 'nomenclatura': 'nitrito'}, {'ânion': 'NO₃⁻', 'nomenclatura': 'nitrato'}, {'ânion': 'N₃⁻', 'nomenclatura': 'azoteto ou azida'}, {'ânion': 'N⁻³', 'nomenclatura': 'nitreto'}, {'ânion': 'PO₃⁻', 'nomenclatura': 'metafosfato'}, {'ânion': 'H₂PO₂⁻', 'nomenclatura': 'hipofosfito'}, {'ânion': 'HPO₃⁻²', 'nomenclatura': 'fosfito'}, {'ânion': 'PO₄⁻³', 'nomenclatura': 'fosfato'}, {'ânion': 'P⁻³', 'nomenclatura': 'fosfeto'}, {'ânion': 'P₂O₇⁻⁴', 'nomenclatura': 'pirofosfato'}, {'ânion': 'P₂O⁻⁴', 'nomenclatura': 'hipofosfato'}, {'ânion': 'S⁻²', 'nomenclatura': 'sulfeto'}, {'ânion': 'SO₄⁻²', 'nomenclatura': 'sulfato'}, {'ânion': 'SO₃⁻²', 'nomenclatura': 'sulfito'}, {'ânion': 'S₂O₃⁻²', 'nomenclatura': 'tiossulfato'}, {'ânion': 'S₂O₄⁻²', 'nomenclatura': 'hipossulfito'}, {'ânion': 'S₂O₈⁻²', 'nomenclatura': 'persulfato'}, {'ânion': 'S₄O₆⁻²', 'nomenclatura': 'tetrationato'}, {'ânion': 'MnO₄⁻', 'nomenclatura': 'permanganato'}, {'ânion': 'MnO₄⁻²', 'nomenclatura': 'manganato'}, {'ânion': 'MnO₃⁻²', 'nomenclatura': 'tetrationato'}, {'ânion': 'OH⁻', 'nomenclatura': 'hidróxido'}, 
    {'ânion': 'H⁻', 'nomenclatura': 'hidreto'}, {'ânion': 'O⁻²', 'nomenclatura': 'óxido'}, {'ânion': 'CrO₄⁻²', 'nomenclatura': 'cromato'}, {'ânion': 'Cr₂O₇⁻²', 'nomenclatura': 'dicromato'}, {'ânion': 'AsO₃⁻³', 'nomenclatura': 'arsenito'}, {'ânion': 'AsO₄⁻³', 'nomenclatura': 'arsenato'}, {'ânion': 'BO₃⁻³', 'nomenclatura': 'borato'}, {'ânion': 'B₄O₇⁻²', 'nomenclatura': 'tetraborato'}, {'ânion': 'SiO₄⁻⁴', 'nomenclatura': 'silicato'}]
    print(formulaion)
    if '⁺' in formulaion or '⁻' in formulaion:
        if '⁺' in formulaion:
            for i, v in enumerate(nomenclatura_cátions):
                if formulaion == v['cátion']:
                    print(f'O íon {v["cátion"]} é chamado de cátion {v["nomenclatura"]}.')
        elif '⁻' in formulaion:
            for i, v in enumerate(nomenclatura_ânions):
                if formulaion == v['ânion']:
                    print(f'O íon {v["ânion"]} é chamado de ânion {v["nomenclatura"]}.')
        elif formulaion not in nomenclatura_cátions and formulaion not in nomenclatura_ânions:
            print('O íon digitado não existe ou não se encontra no banco de dados.')
    else:
        print(f'A espécie química {formulaion} é eletricamente neutra.')
    

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
