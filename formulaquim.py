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
    if i.isdigit() == True:
        formulamostrada.append(i.translate(sub))
separator = ''

funções.cabeçalho(separator.join(formulamostrada))

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

for i in formula:
    if escolha == 1:
        if i.isalpha() == True:
            if i not in formuladados:
                formuladados.append(i)
# for i in formuladados:
#     i = element(f'{i}')
#     translator = Translator()
#     translator.translate(f'{i.name}', scr= 'en', dest= 'pt')

