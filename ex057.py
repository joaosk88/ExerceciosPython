#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0] #aqui o [0] esta fatiando a entrada que o usuario digitou, pega a primeira letra apenas
while sexo != 'F' and sexo != 'M':
    sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').upper().strip()
if sexo == 'M' or sexo == 'F':
 print(f'Sexo {sexo} armazenado com sucesso.')

 #while sexo not in 'MmFf':   (aqui temos uma outra maneira de solucionar esse codigo)