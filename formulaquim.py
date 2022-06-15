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
    # elif escolha == 2: