import funções
from mendeleev import element

formula = list(str(input('Digite a fórmula da substância química: ')).strip())
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
