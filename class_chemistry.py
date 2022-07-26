class Especie:
    def __init__(self, nome, formula):
        self._nome = nome
        self.formula = formula

    def mostrar_nome(self):
        return f'O nome da espécie química é {self._nome}'
    
    def formula_sub(self):
        formula_sub = list()

        for index, caractere in enumerate(self.formula):
            formula_sub.append(caractere)
        for index, caractere in enumerate(formula_sub):
            sub = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
            sob = str.maketrans('0123456789+-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻')
            if str(caractere).isdigit() == True and index != len(formula_sub)-1:
                formula_sub[index] = str(caractere).translate(sub)
            if str(caractere) == '-' and str(formula_sub[index+1]).isdigit() == True or str(caractere) == '+' and str(formula_sub[index+1]).isdigit() == True:
                formula_sub[index] = str(caractere).translate(sob)
                formula_sub[index+1] = str(formula_sub[index+1]).translate(sob)
            if formula_sub[len(formula_sub)-1] == '+' or formula_sub[len(formula_sub)-1] == '-':
                formula_sub.append('1')
        self.formula = ''.join(formula_sub)
    
    def mostrar_dados(self):
        return f'Nome: {self._nome} | Fórmula: {self.formula}'
    
    @property
    def nome(self):
        return self._nome
    
class Ion(Especie, list):
    def __init__(self, nome, formula):
        super().__init__(nome, formula)
        self.carga = ''
    
    def carga_ion(self):
        carga_ion = list()

        for index, caractere in enumerate(self.formula):
            if index == len(self.formula)-2 or index == len(self.formula)-1:
                carga_ion.append(caractere)
        for index, caractere in enumerate(carga_ion):
            num_normal = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻', '0123456789+-')
            carga_ion[index] = str(caractere).translate(num_normal)
        self.carga = ''.join(carga_ion)

class Conjunto:
    def __init__(self, especies):
        self._especies = especies
    
    def __getitem__(self, item):
        return self._especies[item]

    def max_min_carga(self):
        maior = 0
        menor = 0

        for index, especie in enumerate(self._especies):
            especie.formula_sub()
            especie.carga_ion()
            especie.carga = int(especie.carga)
            print(especie[0])
        #     if index == 0:
        #         maior = menor = especie[0].carga
        #     else:
        #         if especie[index].carga > maior:
        #             maior = especie[index].carga
        #         if especie[index].carga < menor:
        #             menor = especie[index].carga
        # print(maior, '- maior')
        # print(menor, '- menor')


     