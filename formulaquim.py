import funções
from mendeleev import element

formulaprinc = list()

formula = list(str(input('Digite a fórmula da substância química: ')).strip())

for i in formula:
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    if i.isalpha() == True:
        formulaprinc.append(i)
    if i.isdigit() == True:
        print(i.translate(sub))
print(formula)
funções.cabeçalho()

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
            i = element(f'{i}')
            print(i.name)
    # elif escolha == 2:
