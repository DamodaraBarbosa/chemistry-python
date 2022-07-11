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


def nomeclaturainorg(formulainorg):
    nomenclatura_cátions = [{'cátion': ['Li', '+'], 'nomenclatura': 'lítio'}, {'cátion': ['Na', '+'], 'nomenclatura': 'sódio'}, {'cátion': ['K', '+'], 'nomenclatura': 'potássio'}, {'cátion': ['Rb', '+'], 'nomenclatura': 'rubídio'}, {'cátion': ['Cs', '+'], 'nomenclatura': 'césio'}, {'cátion': ['Fr', '+'], 'nomenclatura': 'frâncio'}, {'cátion': ['Ag','+'], 'nomenclatura': 'prata'}, {'cátion': ['Cu', '+'], 'nomenclatura': 'cobre ou cuproso'}, {'cátion': ['Au', '+'], 'nomenclatura': 'ouro'}, {'cátion': ['N', 'H', '4', '+'], 'nomenclatura': 'amônio'}, {'cátion': ['Be', '+', '2'], 'nomenclatura': 'berílio'}, {'cátion': ['Mg', '+', '2'], 'nomenclatura': 'magnésio'}, {'cátion': ['Ca', '+', '2'], 'nomenclatura': 'cálcio'}, {'cátion': ['Sr', '+', '2'], 'nomenclatura': 'estrôncio'}, {'cátion': ['Ba', '+', '2'], 'nomenclatura': 'bário'}, {'cátion': ['Rd', '+', '2'], 'nomenclatura': 'rádio'}, {'cátion': ['Zn', '+', '2'], 'nomenclatura': 'zinco'}, {'cátion': ['Cd', '+', '2'], 'nomenclatura': 'cádmio'}, {'cátion': ['Cu', '+', '2'], 'nomenclatura': 'cobre (II) ou cupríco'}, {'cátion': ['Hg', '+', '2'], 'nomenclatura': 'mercúrio (II) ou mercúrico'}, {'cátion': ['Fe', '+', '2'], 'nomenclatura': 'ferro (II) ou ferroso'}, {'cátion': ['Co', '+', '2'], 'nomenclatura': 'cobalto'}, 
    {'cátion': ['Ni', '+', '2'], 'nomenclatura': 'níquel (II) ou niqueloso'}, {'cátion': ['Cr', '+', '2'], 'nomenclatura': 'cromo (II) ou cromoso'}, {'cátion': ['Mn', '+', '2'], 'nomenclatura': 'manganês (II) ou manganoso'}, {'cátion': ['Sn', '+', '2'], 'nomenclatura': 'estanho(II) ou estanhoso'}, {'cátion': ['Pb', '+','2'], 'nomenclatura': 'chumbo (II) ou plumboso'}, {'cátion': ['Ti', '+', '2'], 'nomenclatura': 'titânio (II) ou titanoso'}, {'cátion': ['Pt', '+', '2'], 'nomenclatura': 'platina (II) ou platinoso'}, {'cátion': ['Al', '+', '3'], 'nomenclatura': 'alumínio'}, {'cátion': ['Bi', '+', '3'], 'nomenclatura': 'bismuto'}, {'cátion': ['Au', '+', '3'], 'nomenclatura': 'ouro (III) ou áurico'}, {'cátion': ['Fe', '+', '3'], 'nomenclatura': 'ferro (III) ou férrico'}, {'cátion': ['Co', '+', '3'], 'nomenclatura': 'cobalto (III) ou cobáltico'}, {'cátion': ['Ni', '+', '3'], 'nomenclatura': 'níquel (III) ou niquélico'}, {'cátion': ['Cr', '+', '3'], 'nomenclatura': 'cromo (III) ou crômico'}, {'cátion': ['Sn', '+', '4'], 'nomenclatura': 'estanho (IV) ou estânico'}, {'cátion': ['Pb', '+', '4'], 'nomenclatura': 'chumbo (IV) ou plúmbico'}, {'cátion': ['Ti', '+', '4'], 'nomenclatura': 'titânio (IV) ou titânico'}, {'cátion': ['Pt', '+', '4'], 'nomenclatura': 'platina (IV) ou platínico'}, 
    {'cátion': ['Mn', '+', '4'], 'nomenclatura': 'manganês (IV) ou mangânico'}, {'cátion': ['Cr', '+', '6'], 'nomenclatura':'cromo (VI)'}]
    nomenclatura_ânions = [{'ânion': ['F', '-'], 'nomenclatura': 'fluoreto'}, {'ânion': ['Cl', '-'], 'nomenclatura': 'cloreto'}, {'ânion': ['Br', '-'], 'nomenclatura': 'brometo'}, {'ânion': ['I', '-'], 'nomenclatura': 'iodeto'}, {'ânion': ['Cl', 'O', '-'], 'nomenclatura': 'hipoclorito'}, {'ânion': ['Cl', 'O', '2', '-'], 'nomenclatura': 'clorito'}, {'ânion': ['Cl', 'O', '3', '-'], 'nomenclatura': 'clorato'}, {'ânion': ['Cl', 'O', '4', '-'], 'nomenclatura': 'perclorato'}, {'ânion': ['Br', 'O', '-'], 'nomenclatura': 'hipobromito'}, {'ânion': ['Br', 'O', '₃', '-'], 'nomenclatura': 'bromato'}, {'ânion': ['I', 'O', '-'], 'nomenclatura': 'hipoiodito'}, {'ânion': ['I', 'O', '3', '-'], 'nomenclatura': 'iodato'}, {'ânion': ['I', 'O', '4', '-'], 'nomenclatura': 'periodato'}, {'ânion': ['C', 'N', '-'], 'nomenclatura': 'cianeto'}, {'ânion': ['O', 'C', 'N', '-'], 'nomenclatura': 'cianato'}, {'ânion': ['S', 'C', 'N', '-'], 'nomenclatura': 'tiocianato'}, {'ânion': ['C', 'H', '3', 'C', 'O', 'O', '-'], 'nomenclatura': 'acetato'}, {'ânion': ['C', '2', 'H', '3', 'O', '2', '-'], 'nomenclatura': 'acetato'}, {'ânion': ['C', 'O', '3', '-', '2'], 'nomenclatura': 'carbonato'}, {'ânion': ['H', 'C', 'O', '-', '2'], 'nomenclatura': 'formiato'},  {'ânion': ['H', 'C', 'O', '3', '-'], 'nomenclatura': 'bicarbonato'}, {'ânion': ['C', '2', 'O', '4', '-', '2'], 'nomenclatura': 'oxalato'}, {'ânion': ['C', '2', '-', '2'], 'nomenclatura': 'carbeto ou acetileto'}, 
    {'ânion': ['C', '-', '4'], 'nomenclatura': 'carbeto ou metileto'}, {'ânion': ['N', 'O', '2', '-'], 'nomenclatura': 'nitrito'}, {'ânion': ['N', 'O', '3', '-'], 'nomenclatura': 'nitrato'}, {'ânion': ['N', '3', '-'], 'nomenclatura': 'azoteto ou azida'}, {'ânion': ['N', '-', '3'], 'nomenclatura': 'nitreto'}, {'ânion': ['P', 'O', '3', '-'], 'nomenclatura': 'metafosfato'}, {'ânion': ['H', '2', 'P', 'O', '2', '⁻'], 'nomenclatura': 'hipofosfito'}, {'ânion': ['H', 'P', 'O', '3', '-', '2'], 'nomenclatura': 'fosfito'}, {'ânion': ['P', 'O', '4', '-', '3'], 'nomenclatura': 'fosfato'}, {'ânion': ['P', '-', '3'], 'nomenclatura': 'fosfeto'}, {'ânion': ['P', '2', 'O', '7', '-', '4'], 'nomenclatura': 'pirofosfato'}, {'ânion': ['P', '2', 'O', '-', '4'], 'nomenclatura': 'hipofosfato'}, {'ânion': ['S', '-', '2'], 'nomenclatura': 'sulfeto'}, {'ânion': ['S', 'O', '4', '-', '2'], 'nomenclatura': 'sulfato'}, {'ânion': ['S', 'O', '3', '-', '2'], 'nomenclatura': 'sulfito'}, {'ânion': ['S', '2', 'O', '3', '-', '2'], 'nomenclatura': 'tiossulfato'}, {'ânion': ['S', '2', 'O', '4', '-', '2'], 'nomenclatura': 'hipossulfito'}, {'ânion': ['S', '2', 'O', '8', '-', '2'], 'nomenclatura': 'persulfato'}, {'ânion': ['S', '4', 'O', '6', '-', '2'], 'nomenclatura': 'tetrationato'}, {'ânion': ['Mn', 'O', '4', '-'], 'nomenclatura': 'permanganato'}, {'ânion': ['Mn', 'O', '4', '-', '2'], 'nomenclatura': 'manganato'}, {'ânion': ['Mn', 'O', '3', '-', '2'], 'nomenclatura': 'tetrationato'}, {'ânion': ['O', 'H', '-'], 'nomenclatura': 'hidróxido'}, 
    {'ânion': ['H', '-'], 'nomenclatura': 'hidreto'}, {'ânion': ['O', '-', '2'], 'nomenclatura': 'óxido'}, {'ânion': ['Cr', 'O', '4', '-', '2'], 'nomenclatura': 'cromato'}, {'ânion': ['Cr', '2', 'O', '7', '-', '2'], 'nomenclatura': 'dicromato'}, {'ânion': ['As', 'O','3', '-', '3'], 'nomenclatura': 'arsenito'}, {'ânion': ['As', 'O', '4', '-', '3'], 'nomenclatura': 'arsenato'}, {'ânion': ['B', 'O', '3', '-', '3'], 'nomenclatura': 'borato'}, {'ânion': ['B', '4', 'O', '7', '-', '2'], 'nomenclatura': 'tetraborato'}, {'ânion': ['Si', 'O', '4', '-', '4'], 'nomenclatura': 'silicato'}]

    index_parenteses_inorg = list()
    grupo_positivo = list()
    grupo_negativo = list()

    if '(' and ')' in formulainorg:
        if formulainorg[0] == '(':
            for i, v in enumerate(formulainorg):
                if v == '(' or v == ')':
                    index_parenteses_inorg.append(i)
            print(formulainorg)
            for i, v in enumerate(formulainorg):
                if i > min(index_parenteses_inorg) and i < max(index_parenteses_inorg):
                    grupo_positivo.append(v)
                elif i > max(index_parenteses_inorg):
                    grupo_negativo.append(v)
            for i, v in enumerate(grupo_positivo):
                if v == '1':
                    grupo_positivo.remove(f'{grupo_positivo[i]}')
            for i, v in enumerate(grupo_negativo):
                if i == 0:
                    grupo_negativo.append('-')
                    grupo_negativo.append(v)
                if v == '1':
                    grupo_negativo.remove(f'{grupo_negativo[i]}')
            grupo_negativo.remove(grupo_negativo[0])
            grupo_positivo.append('+')

            for i, v in enumerate(nomenclatura_ânions):
                if grupo_negativo == v['ânion']:
                    print(f'Nome da espécie química: {v["nomenclatura"]} de', end=' ')
            for i, v in enumerate(nomenclatura_cátions):
                if grupo_positivo == v['cátion']:
                    print(f'{v["nomenclatura"]}')
            linha()
        
        for i, v in enumerate(formulainorg):
            if v == '(' or v == ')':
                index_parenteses_inorg.append(i)
        for i, v in enumerate(formulainorg):    
            if i > min(index_parenteses_inorg) and i < max(index_parenteses_inorg):
                grupo_negativo.append(v)
            elif i == 0 or i == len(formulainorg)-1:
                grupo_positivo.append(v)

        grupo_negativo.insert(len(grupo_negativo), '-')
        grupo_positivo.insert(1, '+')

        for i, v in enumerate(formulainorg):
            if v == '(' and str(formulainorg[i-1]).isdigit() == True:
                grupo_negativo.append(formulainorg[i-1])
        for i, v in enumerate(grupo_negativo):
            if v == '1':
                grupo_negativo.remove(f'{grupo_negativo[i]}')
        for i, v in enumerate(nomenclatura_ânions):
            if grupo_negativo == v['ânion']:
                print(f'Nome da espécie química: {v["nomenclatura"]} de', end=' ')
        for i, v in enumerate(nomenclatura_cátions):
            if grupo_positivo == v['cátion']:
                print(f'{v["nomenclatura"]}')
        linha()
    else:
        formulainorg_mod = list()

        for i, v in enumerate(formulainorg):
            if v != '1':
                formulainorg_mod.append(v)
        print(list(formulainorg_mod), '*')
        # for i, v in enumerate(nomenclatura_cátions):
        #     for i, v in enumerate(nomenclatura_cátions[i]['cátion']):
        #         if nomenclatura_cátions[i]['cátion'] in formulainorg_mod:
        #             print('True')
        #         else:
        #             print('False')
        print(formulainorg_mod, 'sem parênteses')
        
                


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
