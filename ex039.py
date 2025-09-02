#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import  date

anoAtual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))


idade = anoAtual - nascimento
alistamento = 18 + nascimento
tempo: float = 18- idade

print('Quem nasceu nos anos {} tem {} anos  em 2025'.format(nascimento, idade))


if  idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(tempo))
    print('Seu alistamento será em {}'.format(alistamento))

elif idade == 18:
    print('Voce tem que se alistar imediatamente')

elif idade >= 60:
    print('Você tem {} anos '.format(idade))
    print('Não precisa mais se alistar')

else:  # aqui fica o caso de idade entre 18 e 59
    print('Você tem {} anos '.format(idade))
    print('Seu alistamento foi no ano {}'.format(alistamento))
    print('Se passaram {} anos que deveria ter se alistado'.format(tempo))








