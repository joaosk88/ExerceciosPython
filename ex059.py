#Crie um programa que leia dois valores e mostre um menu na tela:
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
NewValor = ' '
menu = """
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
"""
print(menu)

menulista = [1, 2, 3, 4, 5]
opcao = 0

opção = int(input(">>>>Escolha uma opção: "))

while opcao != 5:
    if opção == 1:
        print(f'a soma entre {n1} + {n2} é: {n1+n2}')
        print(menu)
        opção= int(input('>>>>Qual é sua opção?:'))

    elif opção ==2:
        print(f'Multiplicando os valores {n1} * {n2 } o valor é: {n1*n2}')
        print(menu)
        opção= int(input('>>>>Qual é sua opção?:'))


    elif opção ==3:
        print(f'Entre os numeros {n1} e {n2} o maior é: {max(n1,n2)}')
        print(menu)
        opção = int(input('>>>>Qual é sua opção?:'))

    elif opção ==4:
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
        print(menu)
        opção = int(input('>>>>Qual é sua opção?:'))

    elif opção ==5:
        print(f'Saindo do programa...')
        break

    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')
        print(menu)
        opção= int(input('>>> Qual a sua opção? '))





