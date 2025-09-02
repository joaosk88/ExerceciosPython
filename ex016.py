#mostra a porção inteira do  numero utilizando a função trunc da biblioteca math
from math import trunc   #aqui estou importando apenas a função trunc que tem como objetivo mostrar a sua porção inteira


a = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(a, trunc(a))) #aqui eu chamo o trunc para a porção inteira do "a"