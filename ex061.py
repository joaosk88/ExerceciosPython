#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA'))
termo = n1
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('Fim')