#escreva um programa qu leia um número inteiro qualquer e peça para o ususario escolher qual será a base de conversão
num = int(input('Digite um numero inteiro:'))

print ('''escolha uma das bases para conversão
[1] converter para BINARIO
[2] converter para OCTAL    
[3] converter para HEXADECIMAL''')

opção = int(input('sua opção: '))

if opção == 1:
    print('{} convertido para BINARIO {}'.format(num,bin(num)[2:]))
elif opção ==2:
    print('{} convertido para OCTAL {}'.format(num,oct(num)[2:]))
elif opção ==3:
    print('{} convertido para HEXADECIMAL {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida')