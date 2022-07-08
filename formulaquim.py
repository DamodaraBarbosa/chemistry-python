import enum
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
função_parêntese = list()

while True:

    formula_mostrada.clear()
    formula_dados.clear()
    formula_contagem.clear()
    formula_contagem_2.clear()
    formula_contagem_3.clear()
    index_repetidos.clear()
    index_parenteses.clear()
    função_parêntese.clear()

    
    formula = list(str(input('Digite a fórmula da substância química: ')).strip())
    
    if formula == ['9','9','9']:
        break
    
    for i, v in enumerate(formula):
        sub = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
        if v.isalpha() == True:
            formula_mostrada.append(v)
        elif v.isdigit() == True and formula[i-1] != '+' or v.isdigit() == True and formula[i-1] != '-':
            formula_mostrada.append(v.translate(sub))
            
        else:
            formula_mostrada.append(v)

    funções.funíon(formula_mostrada)
    
    separator = ''
    funções.cabeçalho(separator.join(formula_mostrada))

    for i in formula:
        if i.isalpha() == True and i.islower() == True:
            formula[formula.index(i)-1:formula.index(i)+1] = [''.join(formula[formula.index(i)-1:formula.index(i)+1])]
    for i in formula:
        if i.isalpha() == True and i not in formula_dados:
            formula_dados.append(i)
    for i, v in enumerate(formula):
        try:
            if i == len(formula)-1 and formula[i].isalpha() == True:
                formula.append('1')
        except AttributeError:
            pass
        if i == len(formula)-2 and formula[i].isalpha() == True and formula[i+1] == '+':
            formula.append(formula.insert(formula.index('+'), '1'))
        if i == len(formula)-2 and formula[i].isalpha() == True and formula[i+1] == '-':
            formula.append(formula.insert(formula.index('-'), '1'))
        if formula[len(formula)-1] == None and formula[len(formula)-2] == '+' or formula[len(formula)-1] == None and formula[len(formula)-2] == '-':
            formula[len(formula)-1] = '1'        
        if formula[i].isalpha() == True and formula[i+1] == ')':
            formula.insert(formula.index(f'{formula[i+1]}'), '1')
    try:
        for i, v in enumerate(formula):
            if v.isalpha() == True and formula[formula.index(v)+1].isalpha() == True:
                index_repetidos.append(i)
    except:
        pass
    
    cont = 0
    for i, v in enumerate(index_repetidos):
        cont += 1
        if i == 0:
            formula.insert(index_repetidos[i]+1, '1')
        else:                    
            formula.insert(index_repetidos[i]+cont, '1')
    for i, v in enumerate(formula):
        try:
            if v.isnumeric() == True and formula[i-1].isnumeric() == True:
                formula[i-1:i+1] = [''.join(formula[i-1:i+1])]
        except AttributeError:
            pass 
    try:
        for i, v in enumerate(formula):
            if v == '(' or v == ')':
                index_parenteses.append(i)
        for i, v in enumerate(formula):
            if i > min(index_parenteses) and i < max(index_parenteses):
                função_parêntese.append(v)
        print(função_parêntese,'ª')
        for i, v in enumerate(formula):
            if i > min(index_parenteses) and v.isdigit() == True and i < max(index_parenteses):
                multiplicacao_parenteses = int(formula[max(index_parenteses)+1])*int(v)
                formula[i] = multiplicacao_parenteses
        try:
            formula.remove(f'{formula[len(formula)-1]}')
            formula.remove('(')
            formula.remove(')')
        except AttributeError:
            pass
        try:
            for i, v in enumerate(formula):
                if formula[0].isalpha() == True and formula[1].isalpha() == True:
                    formula.insert(1, '1')
        except AttributeError:
            pass

        for i, v in enumerate(formula):
            if type(v) == int:
                formula[i] = str(v)
    except ValueError:
        pass
    try:
        for i, v in enumerate(formula):
            if v.isalpha() == True:
                res = str(v*int(formula[i+1]))
                formula_contagem.append(res)
    except:
        pass

    for i, v in enumerate(formula_contagem):
        for i, v in enumerate(formula_contagem[i]):
            formula_contagem_2.append(v)
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
            funções.cabeçalhoop4(''.join(formula_mostrada[0:]))
            if '+' not in formula and '-' not in formula:
                print('A espécie química é eletricamente neutra.')
            else:
                for i in formula:
                    if i == '+' or i == '-':
                        print('É um íon.')
                    if i == '+':
                        print('\033[1;31mCátion\033[m', end=' ')
                    if i == '-':
                        print('\033[1;34mÂnion\033[m', end=' ')
                funções.valencia(formula)
            funções.linha()
            funções.nomenclaturaíon(''.join(formula_mostrada[0:]))
            funções.linha()

        elif escolha == 5:
            print(formula, '*')
            if 'C' not in formula:
                print('Espécie química inorgânica.', '*')
            else:
                index_carbono = list()
                formula = list(formula)
                print(formula, '!')
                carbono_inorg = [['C', '1', 'O', '1'], ['C', '1', 'O', '2'], ['H', '2', 'C', '1', 'O', '3'], ['H', '1', 'C', '1', 'N', '1'], ['C', '1','O', '3'], ['C', '1', 'N', '1'], ['H', '1', 'C', '1', 'O', '3'], ['O', '1', 'C', '1', 'N', '1'], ['C', '2', 'O', '4'], ['S', '1', 'C', '1', 'N', '1'], ['H', '1', 'C', '1', 'O', '1'], ['C'], ['C', '2']]
                for i, v in enumerate(formula):
                    if formula.count('C') == 1 and função_parêntese == []:
                        formula = formula[formula.index('C'):]
                print(formula, '¨¨')
                if formula in carbono_inorg:
                    print('Espécie química inorgânica.', '%')
                elif função_parêntese != []:
                    print(função_parêntese, '@')
                    if função_parêntese in carbono_inorg:
                        print('Espécie química inorgânica.', '#')
                else:
                    print('Espécie química orgânica.')
                    for i, v in enumerate(formula_mostrada):
                        formulagrupamento = ''.join(formula_mostrada[0:len(formula_mostrada)])
            # print(formulagrupamento)
            # funções.grupamentofuncional(formulagrupamento)
            # funções.linha()
                    
        elif escolha == 9:
            funções.linha()
            break
        elif escolha == 0:
            break
        else:
            funções.erro()

    