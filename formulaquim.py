import funções
from mendeleev import element
from googletrans import Translator
from chemspipy import ChemSpider

formulamostrada = list()
formuladados = list()
formulacontagem = list()
formulacontagem2 = list()
formulacontagem3 = list()
indexrepetidos = list()
escolha = ''

while True:

    formulamostrada.clear()
    formuladados.clear()
    formulacontagem.clear()
    formulacontagem2.clear()
    formulacontagem3.clear()
    indexrepetidos.clear()

    formula = list(str(input('Digite a fórmula da substância química: ')).strip())

    if formula == ['9','9','9']:
        break

    for i in formula:
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        if i.isalpha() == True:
            formulamostrada.append(i)
        elif i.isdigit() == True:
            formulamostrada.append(i.translate(sub))
        else:
            formulamostrada.append(i)

    separator = ''
    funções.cabeçalho(separator.join(formulamostrada))

    for i in formula:
        if i.isalpha() == True and i.islower():
            formula[formula.index(i)-1:formula.index(i)+1] = [''.join(formula[formula.index(i)-1:formula.index(i)+1])]
    for i in formula:
        if i.isalpha() == True and i not in formuladados:
            formuladados.append(i)

    cont = 0
    for i, l in enumerate(formula):
        if i == len(formula)-1 and formula[i].isalpha() == True:
                    formula.append('1')
                
    try:
        for i, l in enumerate(formula):
            if l.isalpha() == True and formula[formula.index(l)+1].isalpha() == True:
                        indexrepetidos.append(i)
    except:
        pass

    for i, l in enumerate(indexrepetidos):
        cont += 1
        if i == 0:
            formula.insert(indexrepetidos[i]+1, '1')
        else:                    
            formula.insert(indexrepetidos[i]+cont, '1')

    for i, l in enumerate(formula):
        if l.isnumeric() == True and formula[i-1].isnumeric() == True:
            formula[i-1:i+1] = [''.join(formula[i-1:i+1])]
        
    try:
        for i, l in enumerate(formula):
            if l.isalpha() == True:
                res = str(l*int(formula[i+1]))
                formulacontagem.append(res)
    except:
        pass

    for i, l in enumerate(formulacontagem):
        for i, l in enumerate(formulacontagem[i]):
            formulacontagem2.append(l)
    for i in formulacontagem2:
        if str(i).isalpha() == True and str(i).islower() == True:
            formulacontagem2[formulacontagem2.index(i)-1:formulacontagem2.index(i)+1] = [''.join(formulacontagem2[formulacontagem2.index(i)-1:formulacontagem2.index(i)+1])]
    for i in formulacontagem2:
        if i not in formulacontagem3:
            formulacontagem3.append(i)

    while True:
        try:
            escolha = int(input('Digite a opção desejada: '))
        except ValueError:
            funções.erro()
            while True:
                try:
                    escolha = int(input('Digite a opção desejada: '))
                    break
                except ValueError:
                    funções.erro()

        if escolha == 1:
            funções.cabeçalhoop1()
            for i in formuladados:
                i = element(f'{i}')
                translator = Translator()
                t = translator.translate(f'{i.name}', src= 'en', dest= 'pt')
                print(f'{t.text:<15}', end='     ')
                print(f'{i.atomic_number:<26}', end='    ')
                print(f'{i.atomic_weight:.2f}')
            funções.linha()

        elif escolha == 2:
            print(formula)
            indexparenteses = list()
            formulaparenteses = list()
            formulaparentesesdef = list()

            for i, l in enumerate(formula):
                if l == '(':
                    indexparenteses.append(i)
                if l == ')':
                    indexparenteses.append(i)
            print(indexparenteses)
            for i, l in enumerate(indexparenteses):
                if l not in formulaparenteses:
                    formulaparenteses.append(formula[l+1:])

            print(formulaparenteses)

            for i, l in enumerate(formulaparenteses):
                for i in formulaparenteses[i]:
                    if i not in formulaparentesesdef:
                        formulaparentesesdef.append(i)
            formulaparentesesdef.remove(')')  

            print(formulaparentesesdef, '*')

            indicesparenteses = list()
            for i, l in enumerate(formulaparentesesdef):
                if str(l).isnumeric() == True and l != formulaparentesesdef[len(formulaparentesesdef)-1]:
                    multiply = int(l)*int(formulaparentesesdef[len(formulaparentesesdef)-1])
                    indicesparenteses.append(multiply)
            formulaparentesesdef.remove(f'{formulaparentesesdef[len(formulaparentesesdef)-1]}')
            print(formulaparentesesdef)
            print(indicesparenteses)
            funções.cabeçalhoop2()

            separator = ''
            print(f'{separator.join(formulamostrada):<47}', end='')

            massacumulador = 0
            for i in formulacontagem3:
                elem = element(f'{i}')
                mass = elem.atomic_weight*formulacontagem2.count(i)
                massacumulador += mass
            print(f'{massacumulador:.2f}')
            funções.linha()

        elif escolha == 3:
            funções.cabeçalhoop3()

            for i in formulacontagem3:
                el = element(f'{i}')
                translator = Translator()
                t = translator.translate(f'{el.name}', src= 'en', dest='pt')
                print(f'{t.text:<30}', end='')
                print(formulacontagem2.count(i))
            funções.linha()
        elif escolha == 4:
            
            formulanome = list()

            for i in formulamostrada:
                sub = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
                if i.isalpha() == True:
                    formulanome.append(i)
                elif i.isdigit() == True:
                    formulanome.append(i.translate(sub))
                else:
                    formulanome.append(i)
            cs = ChemSpider('r7nxDXgiGYxrON5yPSjop7PgqAvaPiR2')
            resultado = cs.search(formulanome)
            print(resultado)
            
            for i in formulanome:
                formulanome[0:len(formulanome)] = [''.join(formulanome[0:len(formulanome)])]
        elif escolha == 5:
            funções.linha()
            for i, l in enumerate(formulamostrada):
                formulagrupamento = ''.join(formulamostrada[0:len(formulamostrada)])
            print(formulagrupamento)
            funções.grupamentofuncional(formulagrupamento)
                    
        elif escolha == 9:
            funções.linha()
            break
        elif escolha == 0:
            break
        else:
            funções.erro()

    