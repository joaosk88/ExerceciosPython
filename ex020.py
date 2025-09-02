# embaralhar uma lista utilizando a função "random.shuffle
from  random import shuffle

n1 = input ('Primeiro aluno')
n2 = input ('Segundo aluno')
n3 = input ('Terceiro aluno')
n4 = input ('Quarto aluno')

Lista = [n1, n2, n3, n4]

shuffle(Lista) #aqui estamos embaralhando nossa lista
print(Lista)
