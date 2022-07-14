def linha():
    print('\033[1;33m--\033[m'*38)

def nomenclaturainorg(formulainorg, formulamostrada):
    from mendeleev import element
    from googletrans import Translator
    # nomenclatura dos óxidos
    teste_óxido = list()
    grupo_positivo = list()
    grupo_óxido = list()
    index_digit= list()

    cont = 0 

    print(formulainorg)
    for i, v in enumerate(formulainorg):
        if str(v).isalpha() == True:
            teste_óxido.append(v)
    if len(teste_óxido) == 2 and 'O' in teste_óxido and formulainorg[3] != '2':
        nomenclatura_cátions = [{'cátion': ['Li', '+'], 'nomenclatura': 'lítio', 'carga': '1'}, {'cátion': ['Na', '+'], 'nomenclatura': 'sódio', 'carga': '1'}, {'cátion': ['K', '+'], 'nomenclatura': 'potássio', 'carga': '1'}, {'cátion': ['Rb', '+'], 'nomenclatura': 'rubídio', 'carga': '1'}, {'cátion': ['Cs', '+'], 'nomenclatura': 'césio', 'carga': '1'}, {'cátion': ['Fr', '+'], 'nomenclatura': 'frâncio', 'carga': '1'}, {'cátion': ['Ag','+'], 'nomenclatura': 'prata', 'carga': '1'}, {'cátion': ['Cu', '+'], 'nomenclatura': 'cobre ou cuproso', 'carga': '1'}, {'cátion': ['Au', '+'], 'nomenclatura': 'ouro', 'carga': '1'}, {'cátion': ['N', 'H', '4', '+'], 'nomenclatura': 'amônio', 'carga': '1'}, {'cátion': ['Be', '+', '2'], 'nomenclatura': 'berílio', 'carga': '2'}, {'cátion': ['Mg', '+', '2'], 'nomenclatura': 'magnésio', 'carga': '2'}, {'cátion': ['Ca', '+', '2'], 'nomenclatura': 'cálcio', 'carga': '2'}, {'cátion': ['Sr', '+', '2'], 'nomenclatura': 'estrôncio', 'carga': '2'}, {'cátion': ['Ba', '+', '2'], 'nomenclatura': 'bário', 'carga': '2'}, {'cátion': ['Rd', '+', '2'], 'nomenclatura': 'rádio', 'carga': '2'}, {'cátion': ['Zn', '+', '2'], 'nomenclatura': 'zinco', 'carga': '2'}, {'cátion': ['Cd', '+', '2'], 'nomenclatura': 'cádmio', 'carga': '2'}, {'cátion': ['Cu', '+', '2'], 'nomenclatura': 'cobre (II) ou cupríco', 'carga': '2'}, {'cátion': ['Hg', '+', '2'], 'nomenclatura': 'mercúrio (II) ou mercúrico', 'carga': '2'}, {'cátion': ['Fe', '+', '2'], 'nomenclatura': 'ferro (II) ou ferroso', 'carga': '2'}, {'cátion': ['Co', '+', '2'], 'nomenclatura': 'cobalto', 'carga': '2'}, 
        {'cátion': ['Ni', '+', '2'], 'nomenclatura': 'níquel (II) ou niqueloso', 'carga': '2'}, {'cátion': ['Cr', '+', '2'], 'nomenclatura': 'cromo (II) ou cromoso', 'carga': '2'}, {'cátion': ['Mn', '+', '2'], 'nomenclatura': 'manganês (II) ou manganoso', 'carga': '2'}, {'cátion': ['Sn', '+', '2'], 'nomenclatura': 'estanho(II) ou estanhoso', 'carga': '2'}, {'cátion': ['Pb', '+','2'], 'nomenclatura': 'chumbo (II) ou plumboso', 'carga': '2'}, {'cátion': ['Ti', '+', '2'], 'nomenclatura': 'titânio (II) ou titanoso', 'carga': '2'}, {'cátion': ['Pt', '+', '2'], 'nomenclatura': 'platina (II) ou platinoso', 'carga': '2'}, {'cátion': ['Al', '+', '3'], 'nomenclatura': 'alumínio', 'carga': '3'}, {'cátion': ['Bi', '+', '3'], 'nomenclatura': 'bismuto', 'carga': '3'}, {'cátion': ['Au', '+', '3'], 'nomenclatura': 'ouro (III) ou áurico', 'carga': '3'}, {'cátion': ['Fe', '+', '3'], 'nomenclatura': 'ferro (III) ou férrico', 'carga': '3'}, {'cátion': ['Co', '+', '3'], 'nomenclatura': 'cobalto (III) ou cobáltico', 'carga': '3'}, {'cátion': ['Ni', '+', '3'], 'nomenclatura': 'níquel (III) ou niquélico', 'carga': '3'}, {'cátion': ['Cr', '+', '3'], 'nomenclatura': 'cromo (III) ou crômico', 'carga': '3'}, {'cátion': ['Sn', '+', '4'], 'nomenclatura': 'estanho (IV) ou estânico', 'carga': '4'}, {'cátion': ['Pb', '+', '4'], 'nomenclatura': 'chumbo (IV) ou plúmbico', 'carga': '4'}, {'cátion': ['Ti', '+', '4'], 'nomenclatura': 'titânio (IV) ou titânico', 'carga': '4'}, {'cátion': ['Pt', '+', '4'], 'nomenclatura': 'platina (IV) ou platínico', 'carga': '4'}, 
        {'cátion': ['Mn', '+', '4'], 'nomenclatura': 'manganês (IV) ou mangânico', 'carga': '4'}, {'cátion': ['Cr', '+', '6'], 'nomenclatura':'cromo (VI)', 'carga': '6'}]
        nomenclatura_óxidos = [{'fórmula': ['O'], 'nomenclatura': 'óxido', 'nox': '-2'}, {'fórmula': ['O', '2'], 'nomenclatura': 'peróxido', 'nox': '-1'}, {'fórmula': ['O', '4'], 'nomenclatura': 'superóxido', 'nox': '-1/2'}]

        cont += 1
        
        print(f'A espécie química {formulamostrada} é um óxido')
        for i, v in enumerate(formulainorg):
            if str(v).isdigit() == True:
                index_digit.append(i)
        for i, v in enumerate(formulainorg):
            if i < min(index_digit):
                grupo_positivo.append(v)
                grupo_positivo.append('+')
            if i > min(index_digit) and i <= max(index_digit):
                grupo_óxido.append(v)
        
        # para um óxido
        if str(formulainorg[1]).isdigit() == True and formulainorg[1] == '1' and str(formulainorg[3]).isdigit() == True and formulainorg[3] == '1':
            grupo_positivo.append('2')
            grupo_óxido.remove('1')
        elif str(formulainorg[1]).isdigit() == True and formulainorg[1] != '1' and str(formulainorg[3]).isdigit() == True and formulainorg[3] != '1':
            grupo_positivo.append(formulainorg[max(index_digit)])
            grupo_óxido.remove(formulainorg[len(formulainorg)-1])
        elif str(formulainorg[1]).isdigit() == True and formulainorg[1] != '1' and str(formulainorg[3]).isdigit() == True and formulainorg[3] == '1':
            grupo_óxido.remove(formulainorg[len(formulainorg)-1])
        
        # verificando se o grupo positivo se encontra na lista nomenclatura_cátions
        o1 = 0

        for i, v in enumerate(nomenclatura_cátions):
            if grupo_positivo == nomenclatura_cátions[i]['cátion']:
                o1 += 1
        if o1 == 1:
            for i, v in enumerate(nomenclatura_óxidos):
                if grupo_óxido == nomenclatura_óxidos[i]['fórmula']:
                    print(f'Com nomenclatura: {v["nomenclatura"]} de', end= ' ')
            for i, v in enumerate(nomenclatura_cátions):
                if grupo_positivo == nomenclatura_cátions[i]['cátion']:
                    print(f'{v["nomenclatura"]}.')
        else:
            grupo_positivo.clear()
            grupo_óxido.clear()

            quantidade_oxigênio = 0
            quantidade_elemento = 0
            elemento = ''

            for i, v in enumerate(formulainorg):
                if str(v).isalpha() == True and str(v) != 'O':
                    elemento = v
                    quantidade_elemento = int(formulainorg[i+1])
                if str(v).isdigit() == True and i != 1:
                    quantidade_oxigênio = int(formulainorg[i])
            print('Com nomenclatura: ') 
            if quantidade_oxigênio == 1:
                print('Monóxido de', end=' ')
            elif quantidade_oxigênio == 2:
                print('Dióxido de', end=' ')
            elif quantidade_oxigênio == 3:
                print('Trióxido de', end=' ')
            elif quantidade_oxigênio == 4:
                print('Tetróxido de', end=' ')
            elif quantidade_oxigênio == 5:
                print('Pentóxido de', end=' ')

            el = element(f'{elemento}')
            translator = Translator()
            t = translator.translate(f'{el.name}', src= 'en', dest= 'pt')

            nome_elemento = list(t.text)

            for i, v in enumerate(nome_elemento):
                letra = str.maketrans('ABCDEFGHIJKLMNOPQRSTUWXYZ', 'abcdefghijklmnopqrstuwxyz')
                nome_elemento[0] = str(nome_elemento[0]).translate(letra)
            if quantidade_elemento == 1:
                print(''.join(nome_elemento[0:]))
            elif quantidade_elemento == 2:
                print(f'di{"".join(nome_elemento[0:])}')
            elif quantidade_elemento == 3:
                print(f'tri{"".join(nome_elemento[0:])}')
            elif quantidade_elemento == 4:
                print(f'tetra{"".join(nome_elemento[0:])}')
            elif quantidade_elemento == 5:
                print(f'penta{"".join(nome_elemento[0:])}')
            
    elif len(teste_óxido) == 2 and 'O' in teste_óxido and formulainorg[3] == '2':
        for i, v in enumerate(formulainorg):
            if str(v).isdigit() == True:
                index_digit.append(i)
        for i, v in enumerate(formulainorg):
            if i < min(index_digit):
                grupo_positivo.append(v)
            if i > min(index_digit) and i <= max(index_digit):
                grupo_óxido.append(v)
            

        
        linha()
        
    else:    
        # nomenclatura dos ácidos e bases
        principais_ácidos =  [{'fórmula': ['H', '2', 'S', '1', 'O', '4'], 'nomenclatura': 'ácido sulfúrico'}, {'fórmula': ['H', '4', 'Si', '1', 'O', '4'], 'nomenclatura': 'ácido ortosílico'}, {'fórmula': ['H', '3', 'As', '1', 'O', '4'], 'nomenclatura': 'ácido arseníco'}, {'fórmula': ['H', '3', 'As', '1', 'O', '3'], 'nomenclatura': 'ácido arsenioso'}, {'fórmula': ['H', '3', 'B', '1', 'O', '3'], 'nomenclatura': 'ácido bórico'}, {'fórmula': ['H', '1', 'F', '1'], 'nomenclatura': 'ácido fluorídrico'}, {'fórmula': ['H', '1', 'Cl', '1'], 'nomenclatura': 'ácido clorídrico'}, {'fórmula': ['H', '2', 'C', '1', 'O', '3'], 'nomenclatura': 'ácido carbônico'}, {'fórmula': ['H', '1', 'C', '1', 'N', '1'], 'nomenclatura': 'ácido cianídrico'}, {'fórmula': ['H', '3', 'P', '1', 'O', '4'], 'nomenclatura': 'ácido fosfórico'}, {'fórmula': ['H', '1', 'N', '1', 'O', '3'], 'nomenclatura': 'ácido nítrico'}, {'fórmula': ['H', '1', 'N', '1', 'O', '2'], 'nomenclatura': 'ácido nítroso'}, {'fórmula': ['H', '2', 'S', '1', 'O', '3'], 'nomenclatura': 'ácido sulforoso'}, {'fórmula': ['H', '1', 'N', '1', 'C'], 'nomenclatura': 'ácido isocianídrico'}, {'fórmula': ['H', '1', 'Br', '1'], 'nomenclatura': 'ácido bromídrico'},{'fórmula': ['H', '1', 'I', '1'], 'nomenclatura': 'ácido iodídrico'}, {'fórmula': ['H', '2', 'S', '1'], 'nomenclatura': 'ácido sulfídrico'}, {'fórmula': ['H', '1', 'Cl', '1', 'O', '4'], 'nomenclatura': 'ácido perclórico'}, {'fórmula': ['H', '1', 'Cl', '1', 'O', '3'], 'nomenclatura': 'ácido clórico'}, {'fórmula': ['H', '1', 'Cl', '1', 'O', '2'], 'nomenclatura': 'ácido cloroso'}, {'fórmula': ['H', '1', 'Cl', '1', 'O', '1'], 'nomenclatura': 'ácido hipocloroso'}]
        principais_bases = [{'fórmula': ['Na', '1', 'O', '1', 'H', '1'], 'nomenclatura': 'hidróxido de sódio'}, {'fórmula': ['N', '1', 'H', '3'], 'nomenclatura': 'amônia'}, {'fórmula': ['Ca', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de cálcio'}, {'fórmula': ['Mg', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de magnésio'}, {'fórmula': ['N', '1', 'H', '4', 'O', '1', 'H', '1'], 'nomenclatura': 'hidróxido de amônio'}, {'fórmula': ['K', '1', 'O', '1', 'H', '1'], 'nomenclatura': 'hidróxido de potássio'}, {'fórmula': ['Ba', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de bário'}, {'fórmula': ['Al', '1', '(', 'O', '1', 'H', '1', ')', '3'], 'nomenclatura': 'hidróxido de alumínio'}, {'fórmula': ['Zn', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de zinco'}, {'fórmula': ['Ag', '1', 'O', '1', 'H'], 'nomenclatura': 'hidróxido de prata'}, {'fórmula': ['Li', '1', 'O', '1', 'H'], 'nomenclatura': 'hidróxido de lítio'}, {'fórmula': ['Rb', '1', 'O', '1', 'H'], 'nomenclatura': 'hidróxido de rubídio'}, {'fórmula': ['Cs', '1', 'O', '1', 'H'], 'nomenclatura': 'hidróxido de césio'}, {'fórmula': ['Ni', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de níquel'}, {'fórmula': ['Fe', '1', '(', 'O', '1', 'H', '1', ')', '2'], 'nomenclatura': 'hidróxido de ferro (II) ou ferroso'}, {'fórmula': ['Fe', '1', '(', 'O', '1', 'H', '1', ')', '3'], 'nomenclatura': 'hidróxido de ferro (III) ou férrico'}]
        
        for i, v in enumerate(principais_ácidos):
            if formulainorg == v['fórmula']:
                print(f'A espécie química {formulamostrada} é um ácido.')
                print(f'Com nomenclatura: {v["nomenclatura"]}.')
                cont += 1
        for i, v in enumerate(principais_bases):
            if formulainorg == v['fórmula']:
                print(f'A espécie química {formulamostrada} é uma base.')
                print(f'Com nomenclatura: {v["nomenclatura"]}.')
                cont += 1

        if cont < 1:
        # nomenclatura dos sais 
            nomenclatura_cátions = [{'cátion': ['Li', '+'], 'nomenclatura': 'lítio'}, {'cátion': ['Na', '+'], 'nomenclatura': 'sódio'}, {'cátion': ['K', '+'], 'nomenclatura': 'potássio'}, {'cátion': ['Rb', '+'], 'nomenclatura': 'rubídio'}, {'cátion': ['Cs', '+'], 'nomenclatura': 'césio'}, {'cátion': ['Fr', '+'], 'nomenclatura': 'frâncio'}, {'cátion': ['Ag','+'], 'nomenclatura': 'prata'}, {'cátion': ['Cu', '+'], 'nomenclatura': 'cobre ou cuproso'}, {'cátion': ['Au', '+'], 'nomenclatura': 'ouro'}, {'cátion': ['N', 'H', '4', '+'], 'nomenclatura': 'amônio'}, {'cátion': ['Be', '+', '2'], 'nomenclatura': 'berílio'}, {'cátion': ['Mg', '+', '2'], 'nomenclatura': 'magnésio'}, {'cátion': ['Ca', '+', '2'], 'nomenclatura': 'cálcio'}, {'cátion': ['Sr', '+', '2'], 'nomenclatura': 'estrôncio'}, {'cátion': ['Ba', '+', '2'], 'nomenclatura': 'bário'}, {'cátion': ['Rd', '+', '2'], 'nomenclatura': 'rádio'}, {'cátion': ['Zn', '+', '2'], 'nomenclatura': 'zinco'}, {'cátion': ['Cd', '+', '2'], 'nomenclatura': 'cádmio'}, {'cátion': ['Cu', '+', '2'], 'nomenclatura': 'cobre (II) ou cupríco'}, {'cátion': ['Hg', '+', '2'], 'nomenclatura': 'mercúrio (II) ou mercúrico'}, {'cátion': ['Fe', '+', '2'], 'nomenclatura': 'ferro (II) ou ferroso'}, {'cátion': ['Co', '+', '2'], 'nomenclatura': 'cobalto'}, 
            {'cátion': ['Ni', '+', '2'], 'nomenclatura': 'níquel (II) ou niqueloso'}, {'cátion': ['Cr', '+', '2'], 'nomenclatura': 'cromo (II) ou cromoso'}, {'cátion': ['Mn', '+', '2'], 'nomenclatura': 'manganês (II) ou manganoso'}, {'cátion': ['Sn', '+', '2'], 'nomenclatura': 'estanho(II) ou estanhoso'}, {'cátion': ['Pb', '+','2'], 'nomenclatura': 'chumbo (II) ou plumboso'}, {'cátion': ['Ti', '+', '2'], 'nomenclatura': 'titânio (II) ou titanoso'}, {'cátion': ['Pt', '+', '2'], 'nomenclatura': 'platina (II) ou platinoso'}, {'cátion': ['Al', '+', '3'], 'nomenclatura': 'alumínio'}, {'cátion': ['Bi', '+', '3'], 'nomenclatura': 'bismuto'}, {'cátion': ['Au', '+', '3'], 'nomenclatura': 'ouro (III) ou áurico'}, {'cátion': ['Fe', '+', '3'], 'nomenclatura': 'ferro (III) ou férrico'}, {'cátion': ['Co', '+', '3'], 'nomenclatura': 'cobalto (III) ou cobáltico'}, {'cátion': ['Ni', '+', '3'], 'nomenclatura': 'níquel (III) ou niquélico'}, {'cátion': ['Cr', '+', '3'], 'nomenclatura': 'cromo (III) ou crômico'}, {'cátion': ['Sn', '+', '4'], 'nomenclatura': 'estanho (IV) ou estânico'}, {'cátion': ['Pb', '+', '4'], 'nomenclatura': 'chumbo (IV) ou plúmbico'}, {'cátion': ['Ti', '+', '4'], 'nomenclatura': 'titânio (IV) ou titânico'}, {'cátion': ['Pt', '+', '4'], 'nomenclatura': 'platina (IV) ou platínico'}, 
            {'cátion': ['Mn', '+', '4'], 'nomenclatura': 'manganês (IV) ou mangânico'}, {'cátion': ['Cr', '+', '6'], 'nomenclatura':'cromo (VI)'}]
            nomenclatura_ânions = [{'ânion': ['F', '-'], 'nomenclatura': 'fluoreto', 'carga': '1'}, {'ânion': ['Cl', '-'], 'nomenclatura': 'cloreto', 'carga': '1'}, {'ânion': ['Br', '-'], 'nomenclatura': 'brometo', 'carga': '1'}, {'ânion': ['I', '-'], 'nomenclatura': 'iodeto', 'carga': '1'}, {'ânion': ['Cl', 'O', '-'], 'nomenclatura': 'hipoclorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '2', '-'], 'nomenclatura': 'clorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '3', '-'], 'nomenclatura': 'clorato', 'carga': '1'}, {'ânion': ['Cl', 'O', '4', '-'], 'nomenclatura': 'perclorato', 'carga': '1'}, {'ânion': ['Br', 'O', '-'], 'nomenclatura': 'hipobromito', 'carga': '1'}, {'ânion': ['Br', 'O', '3', '-'], 'nomenclatura': 'bromato', 'carga': '1'}, {'ânion': ['I', 'O', '-'], 'nomenclatura': 'hipoiodito', 'carga': '1'}, {'ânion': ['I', 'O', '3', '-'], 'nomenclatura': 'iodato', 'carga': '1'}, {'ânion': ['I', 'O', '4', '-'], 'nomenclatura': 'periodato', 'carga': '1'}, {'ânion': ['C', 'N', '-'], 'nomenclatura': 'cianeto', 'carga': '1'}, {'ânion': ['O', 'C', 'N', '-'], 'nomenclatura': 'cianato', 'carga': '1'}, {'ânion': ['S', 'C', 'N', '-'], 'nomenclatura': 'tiocianato', 'carga': '1'}, {'ânion': ['C', 'H', '3', 'C', 'O', 'O', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', '2', 'H', '3', 'O', '2', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', 'O', '3', '-', '2'], 'nomenclatura': 'carbonato', 'carga': '2'}, {'ânion': ['H', 'C', 'O', '-', '2'], 'nomenclatura': 'formiato', 'carga': '2'},  {'ânion': ['H', 'C', 'O', '3', '-'], 'nomenclatura': 'bicarbonato', 'carga': '1'}, {'ânion': ['C', '2', 'O', '4', '-', '2'], 'nomenclatura': 'oxalato', 'carga': '2'}, {'ânion': ['C', '2', '-', '2'], 'nomenclatura': 'carbeto ou acetileto', 'carga': '2'}, 
            {'ânion': ['C', '-', '4'], 'nomenclatura': 'carbeto ou metileto', 'carga': '4'}, {'ânion': ['N', 'O', '2', '-'], 'nomenclatura': 'nitrito', 'carga': '1'}, {'ânion': ['N', 'O', '3', '-'], 'nomenclatura': 'nitrato', 'carga': '1'}, {'ânion': ['N', '3', '-'], 'nomenclatura': 'azoteto ou azida', 'carga': '1'}, {'ânion': ['N', '-', '3'], 'nomenclatura': 'nitreto', 'carga': '3'}, {'ânion': ['P', 'O', '3', '-'], 'nomenclatura': 'metafosfato', 'carga': '1'}, {'ânion': ['H', '2', 'P', 'O', '2', '⁻'], 'nomenclatura': 'hipofosfito', 'carga': '1'}, {'ânion': ['H', 'P', 'O', '3', '-', '2'], 'nomenclatura': 'fosfito', 'carga': '2'}, {'ânion': ['P', 'O', '4', '-', '3'], 'nomenclatura': 'fosfato', 'carga': '3'}, {'ânion': ['P', '-', '3'], 'nomenclatura': 'fosfeto', 'carga': '3'}, {'ânion': ['P', '2', 'O', '7', '-', '4'], 'nomenclatura': 'pirofosfato', 'carga': '4'}, {'ânion': ['P', '2', 'O', '-', '4'], 'nomenclatura': 'hipofosfato', 'carga': '4'}, {'ânion': ['S', '-', '2'], 'nomenclatura': 'sulfeto', 'carga': '2'}, {'ânion': ['S', 'O', '4', '-', '2'], 'nomenclatura': 'sulfato', 'carga': '2'}, {'ânion': ['S', 'O', '3', '-', '2'], 'nomenclatura': 'sulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '3', '-', '2'], 'nomenclatura': 'tiossulfato', 'carga': '2'}, {'ânion': ['S', '2', 'O', '4', '-', '2'], 'nomenclatura': 'hipossulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '8', '-', '2'], 'nomenclatura': 'persulfato', 'carga': '2'}, {'ânion': ['S', '4', 'O', '6', '-', '2'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['Mn', 'O', '4', '-'], 'nomenclatura': 'permanganato', 'carga': '1'}, {'ânion': ['Mn', 'O', '4', '-', '2'], 'nomenclatura': 'manganato', 'carga': '2'}, {'ânion': ['Mn', 'O', '3', '-', '2'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['O', 'H', '-'], 'nomenclatura': 'hidróxido', 'carga': '1'}, 
            {'ânion': ['H', '-'], 'nomenclatura': 'hidreto', 'carga': '1'}, {'ânion': ['O', '-', '2'], 'nomenclatura': 'óxido', 'carga': '2'}, {'ânion': ['Cr', 'O', '4', '-', '2'], 'nomenclatura': 'cromato', 'carga': '2'}, {'ânion': ['Cr', '2', 'O', '7', '-', '2'], 'nomenclatura': 'dicromato', 'carga': '2'}, {'ânion': ['As', 'O','3', '-', '3'], 'nomenclatura': 'arsenito', 'carga': '3'}, {'ânion': ['As', 'O', '4', '-', '3'], 'nomenclatura': 'arsenato', 'carga': '3'}, {'ânion': ['B', 'O', '3', '-', '3'], 'nomenclatura': 'borato', 'carga': '3'}, {'ânion': ['B', '4', 'O', '7', '-', '2'], 'nomenclatura': 'tetraborato', 'carga': '2'}, {'ânion': ['Si', 'O', '4', '-', '4'], 'nomenclatura': 'silicato', 'carga': '4'}]

            index_parenteses_inorg = list()
            grupo_positivo = list()
            grupo_negativo = list()

            if '(' and ')' in formulainorg:
                if formulainorg[0] == '(':
                    for i, v in enumerate(formulainorg):
                        if v == '(' or v == ')':
                            index_parenteses_inorg.append(i)
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
                    
                    print(f'A espécie química {formulamostrada} é inorgânica.')
                    for i, v in enumerate(nomenclatura_ânions):
                        if grupo_negativo == v['ânion']:
                            print(f'Com nomenclatura: {v["nomenclatura"]} de', end=' ')
                    for i, v in enumerate(nomenclatura_cátions):
                        if grupo_positivo == v['cátion']:
                            print(f'{v["nomenclatura"]}')        
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
                
                print(f'A espécie química {formulamostrada} é inorgânica.')
                for i, v in enumerate(nomenclatura_ânions):
                    if grupo_negativo == v['fórmula']:
                        print(f'Com nomenclatura: {v["nomenclatura"]} de', end=' ')
                for i, v in enumerate(nomenclatura_cátions):
                    if grupo_positivo == v['cátion']:
                        print(f'{v["nomenclatura"]}')
                linha()
            else:
                formulainorg_mod = list()
                grupo_positivo = list()
                grupo_negativo = list()
                index_digit = list()

                for i, v in enumerate(formulainorg):
                    if v != '1':
                        formulainorg_mod.append(v)
                try:
                    if str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isalpha() == True and str(formulainorg_mod[2]).isalpha() == True:
                        nomenclatura_ânions_sal_X1YZ2 = [{'ânion': ['F', '-'], 'nomenclatura': 'fluoreto', 'carga': '1'}, {'ânion': ['Cl', '-'], 'nomenclatura': 'cloreto', 'carga': '1'}, {'ânion': ['Br', '-'], 'nomenclatura': 'brometo', 'carga': '1'}, {'ânion': ['I', '-'], 'nomenclatura': 'iodeto', 'carga': '1'}, {'ânion': ['Cl', 'O', '-'], 'nomenclatura': 'hipoclorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '2', '-'], 'nomenclatura': 'clorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '3', '-'], 'nomenclatura': 'clorato', 'carga': '1'}, {'ânion': ['Cl', 'O', '4', '-'], 'nomenclatura': 'perclorato', 'carga': '1'}, {'ânion': ['Br', 'O', '-'], 'nomenclatura': 'hipobromito', 'carga': '1'}, {'ânion': ['Br', 'O', '3', '-'], 'nomenclatura': 'bromato', 'carga': '1'}, {'ânion': ['I', 'O', '-'], 'nomenclatura': 'hipoiodito', 'carga': '1'}, {'ânion': ['I', 'O', '3', '-'], 'nomenclatura': 'iodato', 'carga': '1'}, {'ânion': ['I', 'O', '4', '-'], 'nomenclatura': 'periodato', 'carga': '1'}, {'ânion': ['C', 'N', '-'], 'nomenclatura': 'cianeto', 'carga': '1'}, {'ânion': ['O', 'C', 'N', '-'], 'nomenclatura': 'cianato', 'carga': '1'}, {'ânion': ['S', 'C', 'N', '-'], 'nomenclatura': 'tiocianato', 'carga': '1'}, {'ânion': ['C', 'H', '3', 'C', 'O', 'O', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', '2', 'H', '3', 'O', '2', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', 'O', '3', '-'], 'nomenclatura': 'carbonato', 'carga': '2'}, {'ânion': ['H', 'C', 'O', '-'], 'nomenclatura': 'formiato', 'carga': '2'},  {'ânion': ['H', 'C', 'O', '3', '-'], 'nomenclatura': 'bicarbonato', 'carga': '1'}, {'ânion': ['C', '2', 'O', '4', '-'], 'nomenclatura': 'oxalato', 'carga': '2'}, {'ânion': ['C', '2', '-'], 'nomenclatura': 'carbeto ou acetileto', 'carga': '2'}, 
                        {'ânion': ['C', '-'], 'nomenclatura': 'carbeto ou metileto', 'carga': '4'}, {'ânion': ['N', 'O', '2', '-'], 'nomenclatura': 'nitrito', 'carga': '1'}, {'ânion': ['N', 'O', '3', '-'], 'nomenclatura': 'nitrato', 'carga': '1'}, {'ânion': ['N', '3', '-'], 'nomenclatura': 'azoteto ou azida', 'carga': '1'}, {'ânion': ['N', '-'], 'nomenclatura': 'nitreto', 'carga': '3'}, {'ânion': ['P', 'O', '3', '-'], 'nomenclatura': 'metafosfato', 'carga': '1'}, {'ânion': ['H', '2', 'P', 'O', '2', '⁻'], 'nomenclatura': 'hipofosfito', 'carga': '1'}, {'ânion': ['H', 'P', 'O', '3', '-'], 'nomenclatura': 'fosfito', 'carga': '2'}, {'ânion': ['P', 'O', '4', '-'], 'nomenclatura': 'fosfato', 'carga': '3'}, {'ânion': ['P', '-'], 'nomenclatura': 'fosfeto', 'carga': '3'}, {'ânion': ['P', '2', 'O', '7', '-'], 'nomenclatura': 'pirofosfato', 'carga': '4'}, {'ânion': ['P', '2', 'O', '-'], 'nomenclatura': 'hipofosfato', 'carga': '4'}, {'ânion': ['S', '-'], 'nomenclatura': 'sulfeto', 'carga': '2'}, {'ânion': ['S', 'O', '4', '-'], 'nomenclatura': 'sulfato', 'carga': '2'}, {'ânion': ['S', 'O', '3', '-'], 'nomenclatura': 'sulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '3', '-'], 'nomenclatura': 'tiossulfato', 'carga': '2'}, {'ânion': ['S', '2', 'O', '4', '-'], 'nomenclatura': 'hipossulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '8', '-'], 'nomenclatura': 'persulfato', 'carga': '2'}, {'ânion': ['S', '4', 'O', '6', '-'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['Mn', 'O', '4', '-'], 'nomenclatura': 'permanganato', 'carga': '1'}, {'ânion': ['Mn', 'O', '4', '-', '2'], 'nomenclatura': 'manganato', 'carga': '2'}, {'ânion': ['Mn', 'O', '3', '-'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['O', 'H', '-'], 'nomenclatura': 'hidróxido', 'carga': '1'}, 
                        {'ânion': ['H', '-'], 'nomenclatura': 'hidreto', 'carga': '1'}, {'ânion': ['Cr', 'O', '4', '-'], 'nomenclatura': 'cromato', 'carga': '2'}, {'ânion': ['Cr', '2', 'O', '7', '-'], 'nomenclatura': 'dicromato', 'carga': '2'}, {'ânion': ['As', 'O','3', '-'], 'nomenclatura': 'arsenito', 'carga': '3'}, {'ânion': ['As', 'O', '4', '-'], 'nomenclatura': 'arsenato', 'carga': '3'}, {'ânion': ['B', 'O', '3', '-'], 'nomenclatura': 'borato', 'carga': '3'}, {'ânion': ['B', '4', 'O', '7', '-'], 'nomenclatura': 'tetraborato', 'carga': '2'}, {'ânion': ['Si', 'O', '4', '-'], 'nomenclatura': 'silicato', 'carga': '4'}]

                        formulainorg_mod.insert(1, '1')
                        
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        for i, v in enumerate(formulainorg_mod):
                            if i < min(index_digit):
                                grupo_positivo.append(v)
                            if i > min(index_digit) and i <= max(index_digit):
                                grupo_negativo.append(v)
                        
                        grupo_positivo.append('+')
                        grupo_negativo.append('-')

                        for i, v in enumerate(nomenclatura_ânions_sal_X1YZ2):
                            if grupo_negativo == v['ânion']:
                                if v['carga'] != '1':
                                    grupo_positivo.append(v['carga'])
                                    grupo_negativo.append(v['carga'])
                    elif str(formulainorg_mod[1]).isdigit() == True and str(formulainorg_mod[2]).isalpha() == True and str(formulainorg_mod[3]).isalpha() == True:
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        for i, v in enumerate(formulainorg_mod):
                            if i < min(index_digit):
                                grupo_positivo.append(v)
                            if i > min(index_digit) and i <= max(index_digit):
                                grupo_negativo.append(v)

                        grupo_positivo.append('+')
                        grupo_negativo.append('-')
                        grupo_negativo.append(formulainorg_mod[min(index_digit)])

                    elif str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isalpha() == True and str(formulainorg_mod[2]).isdigit() == True and formulainorg_mod[2] == '4':
                        if str(formulainorg_mod[len(formulainorg_mod)-1]).isalpha() == True:
                            formulainorg_mod.append('1')
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        for i, v in enumerate(formulainorg_mod):
                            if i <= min(index_digit):
                                grupo_positivo.append(v)
                            if i > min(index_digit) and i <= max(index_digit):
                                if str(v) != '1':
                                    grupo_negativo.append(v)
                        grupo_positivo.append('+')
                        grupo_negativo.append('-')

                    elif str(formulainorg_mod[2]).isalpha() == True and str(formulainorg_mod[3]).isdigit() == True and str(formulainorg_mod[4]).isalpha() == True and str(formulainorg_mod[5]).isdigit() == True:
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        for i, v in enumerate(formulainorg_mod):
                            if i < min(index_digit):
                                grupo_positivo.append(v)
                            if i > min(index_digit) and i <= max(index_digit):
                                grupo_negativo.append(v)
                        grupo_positivo.append('+')
                        grupo_negativo.append('-')
                        grupo_negativo.append(formulainorg_mod[min(index_digit)])

                    else:
                        if str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isalpha() == True:
                            formulainorg_mod.insert(1, '1')
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        for i, v in enumerate(formulainorg_mod):
                            if i < min(index_digit):
                                grupo_positivo.append(v)
                            if i > min(index_digit) and i < max(index_digit):
                                grupo_negativo.append(v)
                        grupo_positivo.append('+')
                        grupo_positivo.append(formulainorg_mod[max(index_digit)])
                        grupo_negativo.append('-')
                except IndexError:
                    if str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isalpha() == True:
                        for i, v in enumerate(formulainorg_mod):
                            if str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isalpha() == True:
                                formulainorg_mod.insert(1, '1')
                            if str(formulainorg_mod[len(formulainorg_mod)-1]).isalpha() == True:
                                formulainorg_mod.append('1')
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)

                        if formulainorg_mod[min(index_digit)] == formulainorg_mod[max(index_digit)]:
                            nomenclatura_ânions_sal_XY = [{'ânion': ['F', '-'], 'nomenclatura': 'fluoreto', 'carga': '1'}, {'ânion': ['Cl', '-'], 'nomenclatura': 'cloreto', 'carga': '1'}, {'ânion': ['Br', '-'], 'nomenclatura': 'brometo', 'carga': '1'}, {'ânion': ['I', '-'], 'nomenclatura': 'iodeto', 'carga': '1'}, {'ânion': ['Cl', 'O', '-'], 'nomenclatura': 'hipoclorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '2', '-'], 'nomenclatura': 'clorito', 'carga': '1'}, {'ânion': ['Cl', 'O', '3', '-'], 'nomenclatura': 'clorato', 'carga': '1'}, {'ânion': ['Cl', 'O', '4', '-'], 'nomenclatura': 'perclorato', 'carga': '1'}, {'ânion': ['Br', 'O', '-'], 'nomenclatura': 'hipobromito', 'carga': '1'}, {'ânion': ['Br', 'O', '3', '-'], 'nomenclatura': 'bromato', 'carga': '1'}, {'ânion': ['I', 'O', '-'], 'nomenclatura': 'hipoiodito', 'carga': '1'}, {'ânion': ['I', 'O', '3', '-'], 'nomenclatura': 'iodato', 'carga': '1'}, {'ânion': ['I', 'O', '4', '-'], 'nomenclatura': 'periodato', 'carga': '1'}, {'ânion': ['C', 'N', '-'], 'nomenclatura': 'cianeto', 'carga': '1'}, {'ânion': ['O', 'C', 'N', '-'], 'nomenclatura': 'cianato', 'carga': '1'}, {'ânion': ['S', 'C', 'N', '-'], 'nomenclatura': 'tiocianato', 'carga': '1'}, {'ânion': ['C', 'H', '3', 'C', 'O', 'O', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', '2', 'H', '3', 'O', '2', '-'], 'nomenclatura': 'acetato', 'carga': '1'}, {'ânion': ['C', 'O', '3', '-'], 'nomenclatura': 'carbonato', 'carga': '2'}, {'ânion': ['H', 'C', 'O', '-'], 'nomenclatura': 'formiato', 'carga': '2'},  {'ânion': ['H', 'C', 'O', '3', '-'], 'nomenclatura': 'bicarbonato', 'carga': '1'}, {'ânion': ['C', '2', 'O', '4', '-'], 'nomenclatura': 'oxalato', 'carga': '2'}, {'ânion': ['C', '2', '-'], 'nomenclatura': 'carbeto ou acetileto', 'carga': '2'}, 
                            {'ânion': ['C', '-'], 'nomenclatura': 'carbeto ou metileto', 'carga': '4'}, {'ânion': ['N', 'O', '2', '-'], 'nomenclatura': 'nitrito', 'carga': '1'}, {'ânion': ['N', 'O', '3', '-'], 'nomenclatura': 'nitrato', 'carga': '1'}, {'ânion': ['N', '3', '-'], 'nomenclatura': 'azoteto ou azida', 'carga': '1'}, {'ânion': ['N', '-'], 'nomenclatura': 'nitreto', 'carga': '3'}, {'ânion': ['P', 'O', '3', '-'], 'nomenclatura': 'metafosfato', 'carga': '1'}, {'ânion': ['H', '2', 'P', 'O', '2', '⁻'], 'nomenclatura': 'hipofosfito', 'carga': '1'}, {'ânion': ['H', 'P', 'O', '3', '-'], 'nomenclatura': 'fosfito', 'carga': '2'}, {'ânion': ['P', 'O', '4', '-'], 'nomenclatura': 'fosfato', 'carga': '3'}, {'ânion': ['P', '-'], 'nomenclatura': 'fosfeto', 'carga': '3'}, {'ânion': ['P', '2', 'O', '7', '-'], 'nomenclatura': 'pirofosfato', 'carga': '4'}, {'ânion': ['P', '2', 'O', '-'], 'nomenclatura': 'hipofosfato', 'carga': '4'}, {'ânion': ['S', '-'], 'nomenclatura': 'sulfeto', 'carga': '2'}, {'ânion': ['S', 'O', '4', '-'], 'nomenclatura': 'sulfato', 'carga': '2'}, {'ânion': ['S', 'O', '3', '-'], 'nomenclatura': 'sulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '3', '-'], 'nomenclatura': 'tiossulfato', 'carga': '2'}, {'ânion': ['S', '2', 'O', '4', '-'], 'nomenclatura': 'hipossulfito', 'carga': '2'}, {'ânion': ['S', '2', 'O', '8', '-'], 'nomenclatura': 'persulfato', 'carga': '2'}, {'ânion': ['S', '4', 'O', '6', '-'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['Mn', 'O', '4', '-'], 'nomenclatura': 'permanganato', 'carga': '1'}, {'ânion': ['Mn', 'O', '4', '-', '2'], 'nomenclatura': 'manganato', 'carga': '2'}, {'ânion': ['Mn', 'O', '3', '-'], 'nomenclatura': 'tetrationato', 'carga': '2'}, {'ânion': ['O', 'H', '-'], 'nomenclatura': 'hidróxido', 'carga': '1'}, 
                            {'ânion': ['H', '-'], 'nomenclatura': 'hidreto', 'carga': '1'}, {'ânion': ['Cr', 'O', '4', '-'], 'nomenclatura': 'cromato', 'carga': '2'}, {'ânion': ['Cr', '2', 'O', '7', '-'], 'nomenclatura': 'dicromato', 'carga': '2'}, {'ânion': ['As', 'O','3', '-'], 'nomenclatura': 'arsenito', 'carga': '3'}, {'ânion': ['As', 'O', '4', '-'], 'nomenclatura': 'arsenato', 'carga': '3'}, {'ânion': ['B', 'O', '3', '-'], 'nomenclatura': 'borato', 'carga': '3'}, {'ânion': ['B', '4', 'O', '7', '-'], 'nomenclatura': 'tetraborato', 'carga': '2'}, {'ânion': ['Si', 'O', '4', '-'], 'nomenclatura': 'silicato', 'carga': '4'}]

                            for i, v in enumerate(formulainorg_mod):
                                if i < min(index_digit):
                                    grupo_positivo.append(v)
                                if i > min(index_digit) and i < max(index_digit):
                                    grupo_negativo.append(v)
                            grupo_positivo.append('+')
                            grupo_negativo.append('-')
                            for i, v in enumerate(nomenclatura_ânions_sal_XY):
                                if grupo_negativo == v['ânion']:
                                    if v['carga'] != '1':
                                        grupo_positivo.append(v['carga'])
                                        grupo_negativo.append(v['carga'])
                        else:    
                            if str(formulainorg_mod[len(formulainorg_mod)-1]).isdigit() == True and formulainorg_mod[len(formulainorg_mod)-1] != '1':
                                for i, v in enumerate(formulainorg_mod):
                                    if i < min(index_digit):
                                        grupo_positivo.append(v)
                                        grupo_positivo.append('+')
                                        grupo_positivo.append(formulainorg_mod[max(index_digit)])
                                    if i > min(index_digit) and i < max(index_digit):
                                        grupo_negativo.append(v)
                                        grupo_negativo.append('-')
                                        grupo_negativo.append(formulainorg_mod[min(index_digit)])
                                        if '1' in grupo_negativo:
                                            grupo_negativo.remove('1')
                            else:
                                for i, v in enumerate(formulainorg_mod):
                                    if i < min(index_digit):
                                        grupo_positivo.append(v)
                                    if i > min(index_digit) and i <= max(index_digit):
                                        grupo_negativo.append(v)
                                grupo_positivo.append('+')
                                grupo_negativo.append('-')
                                grupo_negativo.append(formulainorg_mod[min(index_digit)])

                                if grupo_negativo.count('1') > 1:
                                    grupo_negativo.remove('1')
                                    grupo_negativo.remove('1')
                    else:
                        for i, v in enumerate(formulainorg_mod):
                            if str(v).isdigit() == True:
                                index_digit.append(i)
                        if str(formulainorg_mod[0]).isalpha() == True and str(formulainorg_mod[1]).isdigit() == True and str(formulainorg_mod[2]).isalpha() == True and formulainorg_mod[2] == formulainorg_mod[len(formulainorg_mod)-1]:
                            formulainorg_mod.append('1')

                            for i, v in enumerate(formulainorg_mod):
                                if str(v).isdigit() == True:
                                    index_digit.append(i)
                            for i, v in enumerate(formulainorg_mod):
                                if i < min(index_digit):
                                    grupo_positivo.append(v)   
                                if i > min(index_digit) and i < max(index_digit):
                                    grupo_negativo.append(v)
                            grupo_positivo.append('+')
                            grupo_positivo.append(formulainorg_mod[max(index_digit)])
                            grupo_positivo.remove('1')
                            grupo_negativo.append('-')
                            grupo_negativo.append(formulainorg_mod[min(index_digit)])
                        else:
                            for i, v in enumerate(formulainorg_mod):
                                if i < min(index_digit):
                                    grupo_positivo.append(v)
                                if i > min(index_digit) and i < max(index_digit):
                                    grupo_negativo.append(v)
                            grupo_positivo.append('+')
                            grupo_positivo.append(formulainorg_mod[max(index_digit)])
                            grupo_negativo.append('-')
                            grupo_negativo.append(formulainorg_mod[min(index_digit)])
                
                print(grupo_positivo, "+ final")
                print(grupo_negativo, "- final")
                
                        
                for i, v in enumerate(nomenclatura_ânions):
                    if grupo_negativo == v['ânion']:
                        print(f'Com nomenclatura: {v["nomenclatura"]} de', end=' ')
                for i, v in enumerate(nomenclatura_cátions):
                    if grupo_positivo == v['cátion']:
                        print(f'{v["nomenclatura"]}')
                linha()  
