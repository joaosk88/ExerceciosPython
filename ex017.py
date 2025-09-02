#importando a função de calcular hipotenusa no math
from math import hypot

a = float(input('Comprimento do cateto oposto'))
b = float(input('Comprimento do cateto adjacente'))

hipotenusa = hypot(a,b)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))