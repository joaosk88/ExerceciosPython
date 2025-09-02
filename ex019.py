#utilizando a biblioteca random sortei um nome aleatorio da lista de alunos
from random import  choice

primeiro = str(input('Primeiro aluno'))
segundo  = str(input('Segundo aluno'))
terceiro = str(input('Terceiro aluno'))
quarto   = str(input('Quarto aluno'))

sorteio = choice([primeiro, segundo, terceiro, quarto])   #função  "random.choice utilizada para sorterar um item aleatorio na lista de alunos

print('O aluno escolhido foi o {}'.format(sorteio))