#crie um programa que leia o comprimento de tres retas e diga ao ususario se elas podem ou não formar um triangulo
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Positivo')
else:
    print('Negativo')