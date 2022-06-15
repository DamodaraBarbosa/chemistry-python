from ntpath import join
import funções
from mendeleev import element
from googletrans import Translator

formulamostrada = list()
formuladados = list()

formula = list(str(input('Digite a fórmula da substância química: ')).strip())

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
    if i.isalpha() == True:
        if i.islower() == True:
            formula[formula.index(i)-1:formula.index(i)+1] = [''.join(formula[formula.index(i)-1:formula.index(i)+1])]
for i in formula:
    if i.isalpha() == True:
        if i not in formuladados:
            formuladados.append(i)

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
    if escolha == 0:
        break
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
    elif escolha == 3:
        cont = 0
        indexrepetidos = list()
        for i, l in enumerate(formula):
            if l.isalpha() == True and formula[formula.index(l)+1].isalpha() == True:
                indexrepetidos.append(i)
            elif i == len(formula) - 1 and l.isalpha():
                formula.insert(i+1, '1')
        for i, l in enumerate(indexrepetidos):
            cont += 1
            if i == 0:
                formula.insert(indexrepetidos[i]+1, '1')
            else:
                formula.insert(indexrepetidos[i]+cont, '1')
        for i, l in enumerate(formula):
            if l.isalpha() == True:
                print(f'{l}'*int(formula[i+1]))

                

                # print(i, end='  ')
            
                # formula.insert(formula.index(l)+1, '1')
                # if formula[formula.index(i)+1].isalpha() == True:
                #     print(i)

                    
        #     formula.insert(i+1, '1')
                # formula.insert(suc, 1)
        print(formula)
    elif escolha == 9:
        funções.linha()
        formulamostrada.clear()
        formuladados.clear()
        formula = list(str(input('Digite a fórmula da substância química: ')).strip())

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
            if i.isalpha() == True:
                if i.islower() == True:
                    formula[formula.index(i)-1:formula.index(i)+1] = [''.join(formula[formula.index(i)-1:formula.index(i)+1])]
        for i in formula:
            if i.isalpha() == True:
                if i not in formuladados:
                    formuladados.append(i)