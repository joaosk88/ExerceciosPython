# analisador de texto

# Solicita ao usuário que digite o nome completo e remove espaços extras no início e no fim
nome = str(input('Digite seu nome completo;')).strip()

# Exibe uma mensagem indicando que o nome será analisado
print('Analisando seu nome')

# Mostra o nome com todas as letras em maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# Mostra o nome com todas as letras em minúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Mostra o total de caracteres digitados, incluindo os espaços
print('Seu nome tem ao todo {} letras'.format(len(nome)))

# Mostra o total de letras, desconsiderando os espaços
print('Seu nome tem {} letras '.format(len(nome) - nome.count(' ')))

#mostra a quantidade de letras apenas do primeiro nome
print('Seu primeito tem {} letras'.format(nome.find(' ')))
