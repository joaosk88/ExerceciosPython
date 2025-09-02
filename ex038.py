#criar um programa que analisa dois numeros e ve qual é o maior, ou se é igual.

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))


if num1 > num2:
    print('O numero {} é maio do que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior do que {}'.format(num2, num1))
elif num1 == num2:
    print('Os dois numeros são iguais')