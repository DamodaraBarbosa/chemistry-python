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
            if str(caractere).isdigit() == True:
                formula_sub[index] = str(caractere).translate(sub)
        self.formula = ''.join(formula_sub)
    
    def mostrar_dados(self):
        return f'Nome: {self._nome} | Fórmula: {self.formula}'
    
    @property
    def nome(self):
        return self._nome
    
class Ion(Especie):
    def __init__(self, nome, formula, carga):
        super().__init__(nome, formula)
        self.carga = carga
     