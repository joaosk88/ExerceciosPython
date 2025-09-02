'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import  date

nascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento

if idade <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MIRIM')
elif idade >= 9 and idade <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: INFANTIL ')
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: SENIOR')
else:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: MASTER')