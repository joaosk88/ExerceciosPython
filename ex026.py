# Faça um programa que leia uma frase pelo teclado e mostre (quantas vezes aparece a letra "A") ( em que posição ela aparece a primeira vez) (em que posição ela aparece por ultimo)

nome = str(input('Digite uma frase: ')).strip().upper()  # o strip serve caso haja espaços no input, ou seja mesmo que o usuario aplique espaços antes de digitar algo, como o strip ele ignora isso
                                                         # o upper vai deixar tudo em maiusculo após o usuario preencher

print('A letra A  apareceu {} vezes na frase.'.format(nome.count('A')))
print('A primiera letra A apareceu na posição {}'.format(nome.find('A')+1)) # o +1 é adicionado com o intuito de iniciarmosn a contagem pela poisção 1 tendo em vista que o python entender que o 0 é o primeiro
print('A ultima letra A apareceu na posição {}'.format(nome.rfind('A')+1))   # aqui o r no find diz para ele começar a procurar da direita para a esquerda