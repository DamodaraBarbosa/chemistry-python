import funções
from mendeleev import element
from googletrans import Translator
from chemspipy import ChemSpider

formula_mostrada = list()
formula_dados = list()
formula_contagem = list()
formula_contagem_2 = list()
formula_contagem_3 = list()
formula_parenteses = list()
index_repetidos = list()
index_parenteses = list()

while True:

    formula_mostrada.clear()
    formula_dados.clear()
    formula_contagem.clear()
    formula_contagem_2.clear()
    formula_contagem_3.clear()
    index_repetidos.clear()
    index_parenteses.clear()
    
    formula = list(str(input('Digite a fórmula da substância química: ')).strip())

    if formula == ['9','9','9']:
        break
    
    for i in formula:
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        if i.isalpha() == True:
            formula_mostrada.append(i)
        elif i.isdigit() == True:
            formula_mostrada.append(i.translate(sub))
        else:
            formula_mostrada.append(i)

    separator = ''
    funções.cabeçalho(separator.join(formula_mostrada))

    for i in formula:
        if i.isalpha() == True and i.islower():
            formula[formula.index(i)-1:formula.index(i)+1] = [''.join(formula[formula.index(i)-1:formula.index(i)+1])]
    for i in formula:
        if i.isalpha() == True and i not in formula_dados:
            formula_dados.append(i)
    
    cont = 0
    for i, l in enumerate(formula):
        if i == len(formula)-1 and formula[i].isalpha() == True:
            formula.append('1')
 
    try:
        for i, l in enumerate(formula):
            if l.isalpha() == True and formula[formula.index(l)+1].isalpha() == True:
                index_repetidos.append(i)
    except:
        pass

    for i, l in enumerate(index_repetidos):
        cont += 1
        if i == 0:
            formula.insert(index_repetidos[i]+1, '1')
        else:                    
            formula.insert(index_repetidos[i]+cont, '1')

    for i, l in enumerate(formula):
        if l.isnumeric() == True and formula[i-1].isnumeric() == True:
            formula[i-1:i+1] = [''.join(formula[i-1:i+1])]
    
    try:
        for i, l in enumerate(formula):
            if l == '(' or l == ')':
                index_parenteses.append(i)
        
        for i, l in enumerate(formula):
            if i > min(index_parenteses) and l.isdigit() == True and i < max(index_parenteses):
                multiplicacao_parenteses = int(formula[max(index_parenteses)+1])*int(l)
                formula[i] = multiplicacao_parenteses

        formula.remove(f'{formula[len(formula)-1]}')
        formula.remove('(')
        formula.remove(')')

        try:
            for i, l in enumerate(formula):
                if formula[0].isalpha() == True and formula[1].isalpha() == True:
                    formula.insert(1, '1')
        except AttributeError:
            pass

        for i, l in enumerate(formula):
            if type(l) == int:
                formula[i] = str(l)
    except ValueError:
        pass
    try:
        for i, l in enumerate(formula):
            if l.isalpha() == True:
                res = str(l*int(formula[i+1]))
                formula_contagem.append(res)
    except:
        pass

    for i, l in enumerate(formula_contagem):
        for i, l in enumerate(formula_contagem[i]):
            formula_contagem_2.append(l)
    for i in formula_contagem_2:
        if str(i).isalpha() == True and str(i).islower() == True:
            formula_contagem_2[formula_contagem_2.index(i)-1:formula_contagem_2.index(i)+1] = [''.join(formula_contagem_2[formula_contagem_2.index(i)-1:formula_contagem_2.index(i)+1])]
    for i in formula_contagem_2:
        if i not in formula_contagem_3:
            formula_contagem_3.append(i)

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
            for i in formula_dados:
                i = element(f'{i}')
                translator = Translator()
                t = translator.translate(f'{i.name}', src= 'en', dest= 'pt')
                print(f'{t.text:<15}', end='     ')
                print(f'{i.atomic_number:<26}', end='    ')
                print(f'{i.atomic_weight:.2f}')
            funções.linha()

        elif escolha == 3:
            
            funções.cabeçalhoop2()

            separator = ''
            print(f'{separator.join(formula_mostrada):<47}', end='')

            massacumulador = 0
            for i in formula_contagem_3:
                elem = element(f'{i}')
                mass = elem.atomic_weight*formula_contagem_2.count(i)
                massacumulador += mass
            print(f'{massacumulador:.2f}')
            funções.linha()

        elif escolha == 2:
            funções.cabeçalhoop3()

            for i in formula_contagem_3:
                el = element(f'{i}')
                translator = Translator()
                t = translator.translate(f'{el.name}', src= 'en', dest='pt')
                print(f'{t.text:<30}', end='')
                print(formula_contagem_2.count(i))
            funções.linha()
        elif escolha == 4:
            
            formulanome = list()

            for i in formula_mostrada:
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
            carbono_inorg = ['CO', 'CO2', 'H2CO3', 'HCN', 'CO3', 'CN', ]
            funções.linha()
            for i, l in enumerate(formula_mostrada):
                formulagrupamento = ''.join(formula_mostrada[0:len(formula_mostrada)])
            print(formulagrupamento)
            funções.grupamentofuncional(formulagrupamento)
                    
        elif escolha == 9:
            funções.linha()
            break
        elif escolha == 0:
            break
        else:
            funções.erro()

    