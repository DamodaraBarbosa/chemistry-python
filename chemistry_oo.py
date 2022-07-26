from class_chemistry import Conjunto, Especie, Ion

sub1 = Especie('Água', 'H2O')
sub2 = Ion('Sulfato', 'SO4-2')
sub3 = Ion('Cálcio', 'Ca+2')
sub4 = Ion('Permanganato', 'MnO4-')
sub5 = Ion('Chumbo (IV)', 'Pb+4')

ions = [sub2, sub3, sub4, sub5]
conjunto_esp = Conjunto(ions)

print(conjunto_esp.max_min_carga())