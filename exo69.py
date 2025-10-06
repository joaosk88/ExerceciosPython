# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
idade = 0
sexo = 'MF '
continuar = 'S'
encerrar = 'N'
pessoas18 = 0
homem = 0
mulher = 0

print('--' *20)
print('SISTEMA DE CADASTRO')
print('--' *20)

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        pessoas18 += 1
        if  sexo == 'M':
            homem += 1
    if sexo == 'F' and idade < 20:
     mulher += 1

    continuar = str(input('Continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('__'*20)
print(f'Total de pessoas com mais de 18 anos: {pessoas18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')













#while sexo == 'F' or sexo == 'F':